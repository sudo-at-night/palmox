FROM redis:6.2-alpine

COPY --chown=redis:redis vol/redis.conf /home/redis/redis.conf
COPY vol/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

WORKDIR /home/redis

CMD [ "redis-server", "/home/redis/redis.conf" ]