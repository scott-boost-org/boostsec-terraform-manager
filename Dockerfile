ARG IMAGE_URL=289082777815.dkr.ecr.us-east-2.amazonaws.com/wolfi-images
ARG IMAGE_VERSION=1.0.62

ARG BASE_SHA=@sha256:6f4402b1b189a3c5026d28f17aaeb28ba25338a5afd3d4d22e0d429d2ad31f87
ARG APK_SHA=@sha256:d70847377d94067b10fe4b11685abd569b461ccb0381ac60fd7b1876b32ec0f2
ARG BUILD_SHA=@sha256:2ac94f56ca6a5084d0733635d154343d5435d9258e976dcd95051ae1cbe4ef87

FROM ${IMAGE_URL}:python-build-${IMAGE_VERSION}${BUILD_SHA} as builder
  RUN --mount=type=secret,id=GITHUB_TOKEN set -ex \
   && git-activate-token-auth

  COPY pyproject.toml \
       poetry.lock \
       /app/

  RUN --mount=type=secret,id=GITHUB_TOKEN --mount=type=ssh set -ex \
   && poetry install --no-root --without dev

  COPY boostsec /app/boostsec

  RUN poetry build \
   && poetry run pip install dist/*.whl --no-deps \
   && rm -rf .venv/src


FROM ${IMAGE_URL}:python-app-${IMAGE_VERSION}${BASE_SHA} as base
  COPY --from=builder /app/.venv /app/.venv
  COPY bin/* /usr/local/bin/
