#!/bin/sh
set -e

# Wait for Redis to start, then create client user with limited permissions
function newUsers() {
    while true
    do
        echo "Waiting for Redis to start..."
        PING_RESULT=$(redis-cli ping)
        case "$PING_RESULT" in
            *NOAUTH*)
                echo "TODO: Initialize users with correct permissions"
                      ;;
            *       ) ;;
        esac
        sleep 5
    done
}

# Replace password in the config with secret
sed -i "s/{{ SERVER_PASSWORD }}/$(cat /run/secrets/redis_server_password)/g" /home/redis/redis.conf
sed -i "s/{{ CLIENT_PASSWORD }}/$(cat /run/secrets/redis_client_password)/g" /home/redis/redis.conf

# first arg is `-f` or `--some-option`
# or first arg is `something.conf`
if [ "${1#-}" != "$1" ] || [ "${1%.conf}" != "$1" ]; then
	set -- redis-server "$@"
fi

# allow the container to be started with `--user`
if [ "$1" = 'redis-server' -a "$(id -u)" = '0' ]; then
	find . \! -user redis -exec chown redis '{}' +
	exec su-exec redis "$0" "$@"
fi

exec "$@" & sleep 1 && newUsers