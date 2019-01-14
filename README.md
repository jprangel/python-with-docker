# python-with-docker

### Task:
Write a python script, which will convert json files to xml files, encrypt and transfer it in a remote location.

Environment: Python, Docker

Description:
Solution should be prepared as two Docker images, 1st to send files, and 2nd to receive them.
Deployment of these containers should be automated using docker-compose or shell script.

Python script on container A:
1. convert all json files to xml 
2. encrypt the files
3. Transfer it to a remote location (container B)

Python script on container B:
1. Receive files
2. Decrypt and store files

So, in other words, pipeline should look like:
Json -> XML -> encryption -> transfer -> decryption -> XML

Acceptance criteria:
Any given Json putted to container A appears in XML form on container B using mentioned pipeline.

## How-to

To execute the project execute:
```
sudo docker-compose up --build
```
Considerations:

1. It was used two JSON files on this project, those files are stored on `instance-a/bucket-r`, if you want to add more JSON files just leave on the folder `bucket-r`.

2. The files converted from JSON to XML and encrypted are stored on `instance-a/bucket-w`.
3. The files decrypted is stored on `instance-b/bucket-w`.
4. As this project it just to a proof of concept, the cryptographic was did by a key gpg (RSA 2048) and the public and the private key was published.
5. As this project it just to a proof of concept, those ssh-keys was published, and the files are transferred by scp command.
6. To access the decrypted XML file in B instance, you should access the container with the command: `docker exec`
7. The image base used in this project can be found on the folder: `image-base/Dockerfile`
8. If you want to execute this project locally, execute:
```
virtualenv -p python3 python-with-docker/instance-a
virtualenv -p python3 python-with-docker/instance-b
source python-with-docker/instance-a/bin/active
source python-with-docker/instance-b/bin/active
python instance-a/src/main.py
python instance-b/src/main.py
```
