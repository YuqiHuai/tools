import subprocess
import os
path = "REPLACE WITH BASE PATH"

tags = """tag1
tag2
tag3"""

tags = tags.strip().split('\n')

for tag in tags[1:]:
    subprocess.run(['cp', '-R', os.path.join(path, tags[0]), os.path.join(path, tag)])
    os.chdir(os.path.join(path, tag))
    subprocess.run(['git', 'checkout', f'tags/{tag}'])

#  docker run --rm -it -v "$(pwd):/home/project" ubuntu_jdk_11
#  cd /home/project
#
# Dockerfile (ubuntu_jdk_11)
# FROM ubuntu
# RUN apt-get update && \ 
#     apt-get install --yes --no-install-recommends \
#     openjdk-11-jdk \
#     maven \
#     git
