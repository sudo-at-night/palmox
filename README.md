# Palmox

![GitHub](https://img.shields.io/github/license/sudo-at-night/palmox?style=for-the-badge)

⚠️ **The project is under constant development, fork it at any point in time but it’s not going to be finished soon.**

# Starting the project

The Project can be run using Docker and docker-compose. Each directory inside of [`src`](#src) however can be treated as a separate repository, which means they can be built and ran independently if provided with alternatives to depend on.

```sh
# Start development Docker containers using docker-compose
docker-compose -f docker/compose.dev.yml up -d
```

# Directories

## `docker`

Docker build and configuration files.

## `src`

Volumes for Docker containers containing source code of each container for day-to-day work.
