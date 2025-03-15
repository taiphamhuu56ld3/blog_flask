# This Makefile will run common task for kotllin
# make : build docker images

BUILD_DIR = build
SCRIPT_DIR = script
DEPLOY_DIR = deployment

# Build docker images, always the FIRST target in this Makefile
build: info
	@bash $(BUILD_DIR)/build_flask_image.sh | tee -a build.log

# Project info
info:
	@echo "make file for build project"

# For deplyment ncd service
deploy: info
	@echo "make file for deployment project"

# For test unit test, function test, system test
test: info
	@echo "For test project unit test, function test, system test"