# Changelog

Rendered by CI and committed back at the end of a release -- do not edit by
hand. Release notes also appear on the GitHub Releases page, one per tag.

## [1.0.5](https://github.com/hyperi-io/ci-test-python-app/compare/v1.0.4...v1.0.5) (2026-10-21)

### Bug Fixes

* **deps:** bump certifi to 2026.10.19 (GHSA-6q48-6c7w-9gw2) ([8870072](https://github.com/hyperi-io/ci-test-python-app/commit/88700726a1b04c3d0603d73b9a4ef38fda627ad8))

## [1.0.4](https://github.com/hyperi-io/ci-test-python-app/compare/v1.0.3...v1.0.4) (2026-10-20)

### Bug Fixes

* bump dulwich, urllib3 past advisories ([c84797d](https://github.com/hyperi-io/ci-test-python-app/commit/c84797d8d11e9558aaec7bcd53ebd07e35456810))
* bump scalo for generate-artefacts ([1b6ba94](https://github.com/hyperi-io/ci-test-python-app/commit/1b6ba941a55db10da34ab8ab27e5fd7cfb3eaab4))
* **ci:** stop this fixture reaching a public registry, adopt org Renovate ([#5](https://github.com/hyperi-io/ci-test-python-app/issues/5)) ([27f6f61](https://github.com/hyperi-io/ci-test-python-app/commit/27f6f61d5bd9e69aa7f4e3efbd0ffc80b95e6692)), closes [hyperi-io/hyperi-ci#79](https://github.com/hyperi-io/hyperi-ci/issues/79)
* **deps:** bump urllib3 to 2.8.0 (CVE-2026-97687/97688/97689) ([4536525](https://github.com/hyperi-io/ci-test-python-app/commit/453652599423f75745fe5f5d01389bdc7313c045))
* drop deprecated .releaserc.yaml (central semantic-release default) ([0413721](https://github.com/hyperi-io/ci-test-python-app/commit/04137214307e9247afbf686126dbf9e43c6b764a))
* enable branch-mode dev-push ([0e3fd4d](https://github.com/hyperi-io/ci-test-python-app/commit/0e3fd4d418e74a4420d3c75c7ba510d6777be630))
* **meta:** use the fleet-wide description format ([9005d62](https://github.com/hyperi-io/ci-test-python-app/commit/9005d621ae3181dc333f71d7135508dddc4c1b75))
* rename legacy publish: config key to release: ([#51](https://github.com/hyperi-io/ci-test-python-app/issues/51)) ([482b1a0](https://github.com/hyperi-io/ci-test-python-app/commit/482b1a078bb811acb2ed145222c0e7ad3d8711b2))

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
