from projen import ProjectType
from projen.python import PythonProject

license_spdx = "Apache-2.0"

project = PythonProject(
    author_email="bfrankovskyi@gmail.com",
    author_name="Bogdan Frankovskyi",
    module_name="example_lambda",
    name="example-lambda-py",
    description="KubeLambda python lambda example",
    license=license_spdx,
    version="0.1.0",
    project_type=ProjectType.APP,
    poetry=False,
    pytest=False,
)

project.add_git_ignore(".mise.toml")
project.add_git_ignore(".secrets.yaml")
project.add_git_ignore("!/LICENSE")

project.synth()

