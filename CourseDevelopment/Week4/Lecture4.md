<<<<<<< Updated upstream
# Course Development Week 4 Documentation for reproducibility

Course Development Week 4 for the Open Science Course for physics students at graduate level. This document is based on the Syllabus.MD.
=======
# Open Science for Physicists, Lecture 4, Documentation for reproducibility

+ Last updated: 27 September 2023
+ Lecturer: @SanliFaez 
>>>>>>> Stashed changes

Date: March/07/2023

Name: Hendrik Snijder @hendelhendel

Open tasks @SanliFaez @erikvansebille
+ Feedback on lecture-tutorial distribution of topics
+ Feedback on lecture format
+ Feedback on tutorial format

## Goal: documenting a real experiment for replication and reproducibility 

Dalle2 & @hendelhendel: the production of science done by a real duck using documents in a scientific environment
![image](https://user-images.githubusercontent.com/93695286/223475265-db677e5b-0933-4529-ace6-ebcb5dacdef9.png)
![image](https://user-images.githubusercontent.com/93695286/223476345-2cdb97a3-96b8-4a6d-9faf-78c7d51340a6.png)


<<<<<<< Updated upstream
## Keywords student familiarity check week 4

|**New Concepts**|**Familiar Concepts**|
|----------------|---------------|
|Data structures and data plans| 
|[FAIR data](https://fairsharing.org/FAIRsharing.WWI10U) |
|Best practices in data visualization|
|GDPR and privacy rules||
|templates and bug reports||
|Persistent identifiers (e.g. DOI)||
|Machine-readable docs||
|Systematic review||
|Scripting||
|Compatibility||
|Dockers-Virtual Environments-Pinning||
|[Open Government Act (Wet Open Overheid)](https://business.gov.nl/regulation/freedom-of-information/)||


## Lecture: Week 4
**Topics in lecture** An overview of best practices on documentation for reproducibility, as well as sharing of open data and open results.
=======
Student teams start with their measurement projects. They will also define the goal of their experiemtn and the analysis procedures, create the proper documentation folder.

*The documentation of each project must be sufficient for another team to replicate the measurement, and reproduce the first teams' results, _only_ based on the shared documentation, _without_ talking to the project owners.*


Summary of [best documentation practices by Wilson et al ](https://doi.org/10.1371/journal.pcbi.1005510)

a. **Data management**
  + Save the raw data. 
  + Ensure that raw data are backed up in more than one location. 
  + Create the data you wish to see in the world. 
  + Create analysis-friendly data. 
  + Record all the steps used to process data. 
  + Anticipate the need to use multiple tables, and use a unique identifier for every record. 
  + Submit data to a reputable DOI-issuing repository so that others can access and cite it.
>>>>>>> Stashed changes

### Lecture format 
**Goal:**  After this lecture students have an overview of best practices in documenting a project. They will also be able to assess what the best route is for them to publish data under FAIR principles.

**Student preparation:** Look in your own archives and check how you stored the documents and data of one of their previous projects, such as your bachelor project. What was the document structure and was it useful? Can someone use your documents to reproduce your results?

**Lecture format** 
+ There will be a presentation about: Machine-readable docs | Systematic review | Persistent identifiers (e.g. DOI) |  GDPR and privacy rules | Scripting
+ A representative of the eScience Centre will give a presentation about best practices in documentation. Students can ask questions and take notes. These are needed in the tutorial. 
    + Suggestion: We can ask Barbara Vreede to give a presentation about "Best practices in writing scientific code" b.m.i.vreede@uu.nl

<<<<<<< Updated upstream
See below for a summary of best practices by
Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, et al. (2017) Good enough practices in scientific computing. PLOS Computational Biology 13(6): e1005510. https://doi.org/10.1371/journal.pcbi.1005510
![image](https://user-images.githubusercontent.com/93695286/223499560-4793bb86-7e39-4cb3-ba79-ee702df4f353.png)
![image](https://user-images.githubusercontent.com/93695286/223499661-14977321-de1f-4e05-907b-026992e2d01a.png)

## Tutorial: Week 4
**!WARNING:**This is a first draft of week 4. An experienced person have to further develop the described assignments in detail. 
From the point of view of students (future physicists). It is a bit dry course material, so a large focus on the tutorial session can help students the most. To let them prepare for future research projects it may be relevant to: create a folder structure of an arbitrary open science project. The same holds for setting up a systematic review or a python environment. 

**Topics in tutorial:**
Data structures and data plans | Best practices in data visualization | GDPR and privacy rules | templates and bug reports | Persistent identifiers (e.g. DOI) |Machine-readable docs | Systematic review | Scripting | Compatibility | Dockers-Virtual Environments-Pinning | [Data publishing routes](https://dmeg.cessda.eu/Data-Management-Expert-Guide/6.-Archive-Publish/Data-publishing-routes)

**Goal:** In this tutorial students will create a template of standard documentation, which they can use later in their career. Furthermore students know how to perform a systematic review.

**Students Preparation:** See lecture preparation

**Grading:** Students hand 3 things: 1. their document structure, 2. project documents 3. the reproduction results of other students project. Everything will be be handed in by a pull request on the course's Github page. In this request, students create a folder with their own name, and add per task their hand-ins. In a README. MD, students explain briefly what they handed in. Not everything has to be perfect, but if all the steps are taken seriously, students can get a pass.

**The Idea:** 

+ **1. Create documents and a folder structure**
  + Create a folder on your computer and call it, STUDENTNUMBER_WEEK4
  + The goal of this exercise is to create a folder structure inside this new folder
  + Create a folder structure as described in box 1 above. Not every step or document in this list can be made, instead create a dummy document. This exercise is to practice good practices and to see all the steps. For example, 3.collaboration.b, can be an empty to-do list in the form of an MD file. When this folder structure is on a repository, one can fork and pull this to-do document to make changes. 
Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, et al. (2017) Good enough practices in scientific computing. PLOS Computational Biology 13(6): e1005510. https://doi.org/10.1371/journal.pcbi.1005510 
  + After you are done, you can fork the repository of this course, and upload your folder with the correct name. Now it is ready to be merged in the main, by a pull request. This process needs to be coordinated by a TA. 
  + A impression of a folder structure with standard documents, (!Not complete!): 
![image](https://user-images.githubusercontent.com/93695286/223513683-add45690-4eee-4d03-84bd-935faeb173f6.png)
=======
 f. **Manuscripts and reports**
   + Write manuscripts using online tools with rich formatting, change tracking, and reference management. 
   + Write the manuscript in a plain text format that permits version control.
   
---
>>>>>>> Stashed changes

## Tutorial: Week 4
	 
### Assignment Executions
1. Form a team of 3 or 4 members and think of a measurement project that satisfies the requirements below.
2. Create an issue on the course repository and specify: a- your measurement goal, b- your team members
3. Clone the course repository on your computer and create your project folder structure on your local repo.
4. Perform your measurement and document it with instructions for replication in a subfolder under [projects](./projects/). Respect the required name convention.
5. Submit your assignment as a merge request to the course repository.
6. After your merge request is accepted, add a hyperlink to your project folder to the main text of your project issue and label it as "Ready for replication". 

### Project minimal requirements 

<<<<<<< Updated upstream
+ **2. Project**
    + In the just created folder structure, students can store project documents. 
    + They are free to do any project they like, which is doable in the tutorial time. Also the project has to be reproducible, so complicated codes, exotic program's etc. are not allowed. 
    + The TA has to approve the project. 

    + **Example project: Prepare a systematic review and write a reproduction manual**
        + Students pick a topic which is relevant for them. Then they write down a search query in google scholar. See: https://guides.library.ucsc.edu/c.php?g=745384&p=5361954
        + Download the first 100 articles in your search queries and store them in Zotero by entering DOI's
        + Download ASReview: https://asreview.nl/
        + Upload The zotero database in ASReview and scan 6 articles on relevance based on their abstract.
        + After that, ASReview will generate an order of articles for you. Go through these ordered articles and stop when articles are not relevant anymore.
        + The resulting articles, i.e., the first few, will be the articles you will study in a systematic review.
        + For reproducibility think of: What choices did I made, What keywords did I used, .. etc? A reproduction should give the same resulting articles. 
        + Are there constrains or systematic errors in the Systematic Review process? (Hint: is Googles ranking for everybody the same?)

    + **Example project: Create a python environment to run a script and write a reproduction manual**
        + Create a pull request on the course Github page.
        + Create a folder called, STUDENTNUMBER_ENV
        + Create a python environment, where you install a package. For example, PYQT5 can be installed. This is a package, used often in experimental physics and is never installed as a standard. 
        + If PyQT is not relevant for you, or a bit to advanced, use Pandas, Numpy and matplotlib to do a simple data manipulation and print some graphs.
        + Create a new python file in this environment and Create something simple with it. Want to do something more advanced? See for example: https://realpython.com/python-pyqt-gui-calculator/ 
        + Or use https://www.youtube.com/watch?v=FVpho_UiDAY to build a GUI
        + If PyQT is not relevant for you, or a bit to advanced(!), use Pandas, Numpy and matplotlib to do a simple data manipulation and print some graphs
        + Upload your environment and your code at the forked repository. 
        + Finish with a pull request.
        + Note, setting up an environment can be hard for the first time: 
            + Open command window and use commands as below
            + see: https://Docs.Conda.Io/Projects/Conda/En/4.6.0/_Downloads/52a95608c49671267e40c689e0bc00ca/Conda-Cheatsheet.Pdf
            + Commands example
            ![image](https://user-images.githubusercontent.com/93695286/223751600-37c678b2-21ea-4223-b715-c9793965e6ce.png)



+ **3. ReproduceReproduceReproduceReproduce**
    + After setting up your folder structure and adding your project documents, other students have to reproduce your results
    + Use the reproducibility feedback as a guide.
    + Pull your reproduced answers in the projects github folders. 


## Information Sources / Bibliography
Best practices in data visualization
+ Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, et al. (2017) Good enough practices in scientific computing. PLOS Computational Biology 13(6): e1005510. https://doi.org/10.1371/journal.pcbi.1005510
+ About the use of colors in scientific comminucation see https://www.nature.com/articles/s41467-020-19160-7 for the article: Crameri, F., Shephard, G.E. & Heron, P.J. The misuse of colour in science communication. Nat Commun 11, 5444 (2020). https://doi.org/10.1038/s41467-020-19160-7

 

Version control
+ Blischak JD, Davenport ER, Wilson G (2016) A Quick Introduction to Version Control with Git and GitHub. PLOS Computational Biology 12(1): e1004668. https://doi.org/10.1371/journal.pcbi.1004668 

GDPR
+ https://www.surf.nl/en/general-data-protection-regulation-gdpr 

Systematic review
+ https://asreview.nl/

Open and FAIR data
+ https://fairsharing.org/FAIRsharing.WWI10U
+ https://dmeg.cessda.eu/Data-Management-Expert-Guide/6.-Archive-Publish/Data-publishing-routes
+ http://opendatahandbook.org/guide/en/
+ https://www.cos.io/initiatives/top-guidelines
=======
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

## Information Sources / Bibliography
+ **Best practices:**  Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, et al. (2017) [Good enough practices in scientific computing](https://doi.org/10.1371/journal.pcbi.1005510) PLOS Computational Biology 13(6): e1005510. 
+ **Version control:** Blischak JD, Davenport ER, Wilson G (2016) [A Quick Introduction to Version Control with Git and GitHub](https://doi.org/10.1371/journal.pcbi.1004668), PLOS Computational Biology 12(1): e1004668.  
+ Data Privacy and GDPR: https://www.surf.nl/en/general-data-protection-regulation-gdpr 
+ General resource on Open and FAIR data
  + https://fairsharing.org/FAIRsharing.WWI10U
  + https://dmeg.cessda.eu/Data-Management-Expert-Guide/6.-Archive-Publish/Data-publishing-routes
  + http://opendatahandbook.org/guide/en/
  + https://www.cos.io/initiatives/top-guidelines
>>>>>>> Stashed changes
