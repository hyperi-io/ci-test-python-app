## [1.0.3](https://github.com/hyperi-io/ci-test-python-app/compare/v1.0.2...v1.0.3) (2026-04-30)


### Bug Fixes

* add dev dep group with ruff/ty/pytest so CI can spawn ruff ([1791712](https://github.com/hyperi-io/ci-test-python-app/commit/1791712c522d8d06e35ac9438ea52d4073da277b))
* add Dockerfile + GHCR container config (canary for hyperi-ci v1.13.1+ container pipeline) ([78902c5](https://github.com/hyperi-io/ci-test-python-app/commit/78902c5ec6c4fb3f94050948e457de3f7dfe6b5a))
* add pytest-cov to dev deps so coverage flags work ([483bb5e](https://github.com/hyperi-io/ci-test-python-app/commit/483bb5ed150b049a0618ae17a8dda4251847dfad))
* declare hyperi-pylib[metrics] for psutil at import time ([de4d6d9](https://github.com/hyperi-io/ci-test-python-app/commit/de4d6d927a10c0da4150a7f8967801528fad852a))
* greenfield as ci-test-python-app — hyperi-pylib + Dockerfile + GHCR push ([600fd98](https://github.com/hyperi-io/ci-test-python-app/commit/600fd9849ba3311bb19fcbb23dc3a1a8e5b93bc6))
* refresh init output and target=oss + container config ([78b9c18](https://github.com/hyperi-io/ci-test-python-app/commit/78b9c18b7d8e2e157285b4a1085be5c05884be76))

## [1.0.2](https://github.com/hyperi-io/ci-test-python-cli/compare/v1.0.1...v1.0.2) (2026-03-02)


### Bug Fixes

* add build.type to config ([eb7a5e6](https://github.com/hyperi-io/ci-test-python-cli/commit/eb7a5e6f436534b9bf15de22b904a2228e763048))

## [1.0.1](https://github.com/hyperi-io/ci-test-python-cli/compare/v1.0.0...v1.0.1) (2026-03-02)


### Bug Fixes

* remove container requirement for default GH runner ([fbf4ead](https://github.com/hyperi-io/ci-test-python-cli/commit/fbf4ead1347b5a750268d57ccea6a637e7fe2393))

# 1.0.0 (2026-03-02)


### Features

* initial scaffold for CI test project ([99dee41](https://github.com/hyperi-io/ci-test-python-cli/commit/99dee41cd620276ee7f799cc00657a8cf4c47a1e))
