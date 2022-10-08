# DockerBasics

1. For Docker virtualization should be enabled

![image](https://user-images.githubusercontent.com/114802910/194708764-479048a5-92bc-4965-bf0c-f83be41e6b7a.png)

2. **docker -v**

   Gives the latest installest docker version in your machine.
   ![image](https://user-images.githubusercontent.com/114802910/194708808-1cb56f28-2731-411b-8cfa-203e072a1d9e.png)


**3. docker pull <image name>**
  
  This command pulls the docker image from docker hub in the local system
  ![image](https://user-images.githubusercontent.com/114802910/194709248-068fb039-703a-4653-ac05-a76ae3f412c7.png)


**4. docker images**
  
  This command gives a list of image downloaded from docker hub to local 
  ![image](https://user-images.githubusercontent.com/114802910/194709276-64db7e64-f109-4311-b3b4-056ab539f60a.png)


**5. docker run -d -p 80:80 <image name>**
  
  This command is used to run the docker image. When we run a docker image, a container is created inside which this image runs.
  ![image](https://user-images.githubusercontent.com/114802910/194709982-f44da00c-4883-4403-9510-691a58d2a599.png)

**6. docker ps**
  
  This command shows the status of all running containers only.
  ![image](https://user-images.githubusercontent.com/114802910/194710106-ed90eb1c-bfc7-4da5-92cb-2df8c7085aa7.png)

**7. docker stop <containerid>**
  
  This command is used to stop a container. But the image still exists as we haven't deleted docker image from local system yet.
  ![image](https://user-images.githubusercontent.com/114802910/194710148-46048cdd-8771-4b54-b4c5-576266c691e4.png)

**8. docker image rm -f <imageid>**
  
  This command is used to forcefully remove a image from local.
  ![image](https://user-images.githubusercontent.com/114802910/194710385-0e8fa6ca-9b3e-4758-8cb9-c79410375ff4.png)


**# Commands to create a docker image and then uploading it in docker hub**
  
**9.  How to create Docker file in VScode**
  
  ![image](https://user-images.githubusercontent.com/114802910/194710518-532cfa52-ddb4-4d81-8bdd-f43e115194bc.png)

**10. docker build -t username/dockername .**

    This command is used to build the docker image. We try to create the name using username and then the image name user want.
    ![image](https://user-images.githubusercontent.com/114802910/194710672-0eec5df5-34cf-4e83-9075-bf439f5e7fd3.png)

    ![image](https://user-images.githubusercontent.com/114802910/194710680-b246b202-adf6-499a-abbf-e2ac28cbacf0.png)


**11. docker push username/dockername:latest**
  
  This command is used to push the docker image locally build into docker hub.
  ![image](https://user-images.githubusercontent.com/114802910/194710727-aa333564-e9a9-4517-abac-29478bd01302.png)
  
 **12. docker restart <container id>**
  
    This command first stops the container and then automatically start it back.
   ![image](https://user-images.githubusercontent.com/114802910/194711485-20904cbe-6ff9-456a-8334-3c5ee2f5e0b3.png) 

  
**13. docker ps -a**
  
    This command lists all the containers(running + exited)
    ![image](https://user-images.githubusercontent.com/114802910/194711550-c6f473fe-d03e-493b-afd2-044ca8a73341.png)
  
**14. docker top <containerid>**
  
    This command shows the list of processes running inside a container
    ![image](https://user-images.githubusercontent.com/114802910/194711637-c98fd37d-4e71-46b5-b88d-8d5f862f88c6.png)
  
**15. docker inspect <imageid>**
  
  This command shows the low level info of the image
  ![image](https://user-images.githubusercontent.com/114802910/194711726-5d3bb0c1-f82c-4590-97e0-5be02c387005.png)



  

**NOTE**
  
Below is the docker image locally build and uploaded in docker hub.
https://hub.docker.com/repository/docker/shalinitiwari2701/dockerbasics

**Output of the fastAPI**
  
![image](https://user-images.githubusercontent.com/114802910/194710976-83b0ffdc-352c-4af4-9841-f0eb05e67bc3.png)

