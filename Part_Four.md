## Part 4: Deploying container on IBM Kubernetes Service
#### Steps
1. Log in to your IBM Cloud account and create a [Kubernetes Service](https://cloud.ibm.com/kubernetes/catalog/create)
2. Intall [IBM Cloud CLI](https://cloud.ibm.com/docs/cli/reference/ibmcloud/download_cli.html#shell_install):
  - Check whether Cloud CLI is installed: 
  - > ibmcloud --version 
  - Check installed plugins: 
  - > ibmcloud plugin list
  - Install plugins if not installed already:
  - > ibmcloud plugin install dev
  - > ibmcloud plugin install kubernetes-service
  - > ibmcloud plugin install container-registry
3. Follow the [Openshift](https://developer.ibm.com/technologies/containers/tutorials/deploy-python-app-to-openshift-cluster-source-to-image/) tutorial for next steps
