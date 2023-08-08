# Open Science for Physicists, Lecture 4, Reproducibility

+ Last updated: 8 August 2023
+ Lecturer: @SanliFaez 

#### Contributors: 
+ Erik van Sebille @erikvansebille
+ Hendrik Snijder @hendelhendel

## Goal: Documentation for reproducibility

![Project documentation illustrated as a roadmap](reproducibility.jpg)
[The Turing Way project](https://the-turing-way.netlify.app/reproducible-research/reproducible-research) illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: 10.5281/zenodo.3332807.

### Lecture format
During weeks 4 and 5 of the course, students form teams to make a small computer-assisted measurement project, with a focus on reproducibility of the results. Week 4 is mainly for setting up the project and its documentation, and week 5 is dedicated to reproducing the project by other teams and writing a peer-feedback report. 

Students will also get a tour or [Lili's proto lab](https://www.uu.nl/lpl) and get familiar with various rapid-prototyping tool, which they can use to enhance their projects.

**The 5-minutes exercise:** Chose a previous report (at least 6 months old) you have written (e.g. your bachelor project) and pick a random graph that you have generated. In 5 minutes, find the data corresponding to that graph and regenerate it. What was the document structure and was it useful? Can someone else use your documents to reproduce your results?

---
Summary of [best documentation practices by Wilson et al ](https://doi.org/10.1371/journal.pcbi.1005510)

a. **Data management**
  + Save the raw data. 
  + Ensure that raw data are backed up in more than one location. 
  + Create the data you wish to see in the
  world. 
  + Create analysis-friendly data. 
  + Record all the steps used to process data. 
  + Anticipate the need to use multiple
  tables, and use a unique identifier for every record. 
  + Submit data to a reputable DOI-issuing repository so that others
  can access and cite it.

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
   



## Tutorial: Open hardware and reproducibility 
**Tutorial Goal:**
The main goal of this tutorial is to use open hardware resources, to create a measurement setup for a physics-related concept or sensing application. Documentation of this project will be used for reproducing its result and practicing the essential steps of good documentation.

**Admissable projects:** 
All types of measurement projects are allowed, provided they satisfy the following criteria:
+ The measurements are done via a microcontroller, computer hardware, or digitized sensors.
+ At least one plot is created based on the measured data and used for the goal of the measurements.
+ The plot data is analyzed with a computer script.
+ The measurements are safe for the user and can be executed in maximum 15 minutes.
+ The measurements results and conclusions can be independently verified by a different team without face to face interaction with the project team.
+ The TA approves the project. 
+ Every assignment should be handed in by a pull-request on the course Gitlab repository, inside the `/projects` subfolder. 

Some examples are provided in the [accompanying file](OpenHardwareExamples.md). It is allowed to bring in measurement projects that you have executed before in other courses, provided that they can be publisehd under an open-source license. Your projects might be added to the examples for the following year.

**Reproducing results:**
In the following week, another student team will try to reproduce your measurement and write a feedback report based on the [peer-evaluation template](../Week5/peer_evaluation_FORWHICHPROJECT.md)

## Information Sources / Bibliography
+ **Best practices:**  Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, et al. (2017) [Good enough practices in scientific computing](https://doi.org/10.1371/journal.pcbi.1005510) PLOS Computational Biology 13(6): e1005510. 
+ **Version control:** Blischak JD, Davenport ER, Wilson G (2016) [A Quick Introduction to Version Control with Git and GitHub](https://doi.org/10.1371/journal.pcbi.1004668), PLOS Computational Biology 12(1): e1004668.  
+ Data Privacy and GDPR: https://www.surf.nl/en/general-data-protection-regulation-gdpr 
+ General resource on Open and FAIR data
  + https://fairsharing.org/FAIRsharing.WWI10U
  + https://dmeg.cessda.eu/Data-Management-Expert-Guide/6.-Archive-Publish/Data-publishing-routes
  + http://opendatahandbook.org/guide/en/
  + https://www.cos.io/initiatives/top-guidelines
