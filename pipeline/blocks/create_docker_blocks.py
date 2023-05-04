from prefect.infrastructure.docker import DockerContainer

# programmatic way for creating Docker container block instead creation in the UI
docker_block = DockerContainer(
    image="docker-username/prefect:tagname",  # insert your image here
    image_pull_policy="ALWAYS",
    auto_remove=True,
)

docker_block.save("docker-block-name", overwrite=True)