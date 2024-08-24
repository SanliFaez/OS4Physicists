# Open Science for Physicists, Lecture 4, Documentation for reproducibility

+ Last updated: 27 September 2023
+ Lecturer: @SanliFaez 

#### Contributors: 
+ Erik van Sebille @erikvansebille
+ Hendrik Snijder @hendelhendel


## Goal: documenting a real experiment for replication and reproducibility 

![Project documentation illustrated as a roadmap](reproducibility.jpg)
[The Turing Way project](https://the-turing-way.netlify.app/reproducible-research/reproducible-research) illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: 10.5281/zenodo.3332807.

Student teams start with their measurement projects. They will also define the goal of their experiemtn and the analysis procedures, create the proper documentation folder.

*The documentation of each project must be sufficient for another team to replicate the measurement, and reproduce the first teams' results, _only_ based on the shared documentation, _without_ talking to the project owners.*

---

Summary of [best documentation practices by Wilson et al ](https://doi.org/10.1371/journal.pcbi.1005510)

a. **Data management**
  + Save the raw data. 
  + Ensure that raw data are backed up in more than one location. 
  + Create the data you wish to see in the world. 
  + Create analysis-friendly data. 
  + Record all the steps used to process data. 
  + Anticipate the need to use multiple tables, and use a unique identifier for every record. 
  + Submit data to a reputable DOI-issuing repository so that others can access and cite it.

b. **Software**
  + Place a brief explanatory comment at the start of every program. 
  + Decompose programs into functions. 
  + Be ruthless about eliminating duplication. 
  + Always search for well-maintained software libraries that do what you need. 
  + Test libraries before relying on them. 
  + Give functions and variables meaningful names. 
  + Make dependencies and requirements explicit. 
  + Do not comment and uncomment sections of code to control a program's behavior.
  + Provide a simple example or test data set. 
  + Submit code to a reputable DOI-issuing repository.

c. **Collaboration**
  + Create an overview of your project. 
  + Create a shared "to-do" list for the project. 
  + Decide on communication strategies. 
  + **Make the license explicit.**
  + Make the project citable. 

d. **Project organization**
  + **Put each project in its own directory, which is named after the project.** 
  + Put text documents associated with the project in the `/doc` directory. 
  + Put raw data and metadata in a data directory and files generated during cleanup and analysis in a results directory. 
  + Put project source code in the src directory. 
  + Put external scripts or compiled programs in the bin directory. 
  + Name all files to reflect their content or function.
   
e. **Keeping track of changes** 
  + Back up (almost) everything created by a human being as soon as it is created. 
  + Keep changes small. 
  + Share changes frequently. 
  + Create, maintain, and use a checklist for saving and sharing changes to the project.
  + Store each project in a folder that is mirrored off the researcher's working machine. 
  + Add a file called CHANGELOG.txt to the project's docs subfolder. 
  + Copy the entire project whenever a significant change has been made. 
  + Use a version control system.

 f. **Manuscripts and reports**
   + Write manuscripts using online tools with rich formatting, change tracking, and reference management. 
   + Write the manuscript in a plain text format that permits version control.
   
---

## Tutorial: Week 4
	 
### Assignment Executions
1. Form a team of 3 or 4 members and think of a measurement project that satisfies the requirements below.
2. Create an issue on the course repository using the [issue template for the measurement project](./issue_templates/measurement_project.md) and label it as "project in progress".
3. Clone the course repository on your computer and create your project folder structure on your local repo. You can use the provided folder structure but do not forget to personalize all readme files.
4. Perform your measurement and document it with instructions for replication in a subfolder under [projects](./projects/). Respect the required name convention.
5. Submit your assignment as a merge request to the course repository.
6. After your merge request is accepted, add a hyperlink to your project folder in your project issue and label the issue as "ready to reproduce". 

### Project minimal requirements 

+ Use an electronic sensor to measure a physical quantity or to perform a demonstration experiment. You can use any type of open hardware controller boards or a smartphone using the [phyphox app](https://phyphox.org/)
+ The measurements should be recorded electronically and digitally.  
    + you must perform at least one measurement to prove the functioning of your experiment and report the result. 
    + The measurements are done via a microcontroller, computer hardware, or digitally-logged sensors.
	+ At least one plot is created based on the measured data and used for the goal of the measurements.
	+ The plot data is analyzed with a computer script.
	+ The measurements are safe for other students can and can be executed in maximum 15 minutes.
	+ The measurements results and conclusions can be independently verified by a different team without face to face interaction with the project team.
	+ The TA or coordinator approves the project. 
    + The analysis code should use the measured data to create your anticipated result, and preferably a plot of your data.
    + a third person should be able to reproduce your measurement(s) based on your documentation.  
+ Document the measurements you have done for reproducibility and prepare the instructions on how to:
	0. safely operate your setup
	1. replicate your results based on new measurements
	2. reproduce your results based on the raw data that you have obtained
	 
#### Reproducing results:
In the following week, another student team will try to reproduce your measurement and write a feedback report based on the [peer-evaluation template](../Lectures/Week5/peer_evaluation_COMMENTonISSUE.md)
	 
### Additional recommendations
+ Check these [peer review instructions](../Lectures/Week5/peer_evaluation_COMMENTonISSUE.md) before finalizing your documentation. Other teams will be asked to follow these instructiosn for reviewing and replicating your work.
+ Invite other people to check your documentation for clarity and sufficiency.
+ Separate the instructions for reproducing your results from those for replicating the measurement
---
 
## Information Sources / Bibliography
+ **Best practices:**  Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, et al. (2017) [Good enough practices in scientific computing](https://doi.org/10.1371/journal.pcbi.1005510) PLOS Computational Biology 13(6): e1005510. 
+ **Version control:** Blischak JD, Davenport ER, Wilson G (2016) [A Quick Introduction to Version Control with Git and GitHub](https://doi.org/10.1371/journal.pcbi.1004668), PLOS Computational Biology 12(1): e1004668.  
+ Data Privacy and GDPR: https://www.surf.nl/en/general-data-protection-regulation-gdpr 
+ General resource on Open and FAIR data
  + https://fairsharing.org/FAIRsharing.WWI10U
  + https://dmeg.cessda.eu/Data-Management-Expert-Guide/6.-Archive-Publish/Data-publishing-routes
  + http://opendatahandbook.org/guide/en/
  + https://www.cos.io/initiatives/top-guidelines

