# Course Development Week 4 Documentation for reproducibility

Course Development Week 4 for the Open Science Course for physics students at graduate level. This document is based on the Syllabus.MD.

Date: March/07/2023

Name: Hendrik Snijder @hendelhendel

Open tasks @SanliFaez @erikvansebille
+ Feedback on lecture-tutorial distribution of topics
+ Feedback on lecture format
+ Feedback on tutorial format

## Goal: Documentation for reproducibility

Dalle2 & @hendelhendel: the production of science done by a real duck using documents in a scientific environment
![image](https://user-images.githubusercontent.com/93695286/223475265-db677e5b-0933-4529-ace6-ebcb5dacdef9.png)
![image](https://user-images.githubusercontent.com/93695286/223476345-2cdb97a3-96b8-4a6d-9faf-78c7d51340a6.png)


## Keywords student familiarity check week 4

|**New Concepts**|**Familiar Concepts**|
|----------------|---------------|
|Data structures and data plans| 
|Best practices in data visualization|
|GDPR and privacy rules||
|templates and bug reports||
|Persistent identifiers (e.g. DOI)||
|Machine-readable docs||
|Systematic review||
|Scripting||
|Compatibility||
|Dockers-Virtual Environments-Pinning||


## Lecture: Week 4
**Topics in lecture** An overview of best practises on documentation for reproducibility.

### Lecture format 
**Goal:**  After this lecture students have an overview of best practices in documenting.

**Student preparation:** Look in your own archives and check how you stored the documents of one of their previous projects, such as your bachelor project. What was the document structure and was it useful? Can someone use your documents to reproduce your results?

**Lecture format** 
+ There will be a presentation about: Machine-readable docs | Systematic review | Persistent identifiers (e.g. DOI) |  GDPR and privacy rules | Scripting
+ A representative of the eScience Centre will give a presentation about best practises in documantion. Students can ask questions and take notes. These are needed in the tutorial. 
    + Suggestion: We can ask Barbara Vreede to give a presentation about "Best practices in writing scientific code" b.m.i.vreede@uu.nl

See below for a summary of best practices by
Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, et al. (2017) Good enough practices in scientific computing. PLOS Computational Biology 13(6): e1005510. https://doi.org/10.1371/journal.pcbi.1005510
![image](https://user-images.githubusercontent.com/93695286/223499560-4793bb86-7e39-4cb3-ba79-ee702df4f353.png)
![image](https://user-images.githubusercontent.com/93695286/223499661-14977321-de1f-4e05-907b-026992e2d01a.png)

## Tutorial: Week 4
**!WARNING:**This is a first draft of week 4. An experienced person have to further develop the described assignments in detail. 
From the point of view of students (future physicists). It is a bit dry course material, so a large focus on the tutorial session can help students the most. To let them prepare for future research projects it may be relevant to: create a folder structure of an arbitrary open science project. The same holds for setting up a systematic review or a python environment. 

**Topics in tutorial:**
Data structures and data plans | Best practices in data visualization | GDPR and privacy rules | templates and bug reports | Persistent identifiers (e.g. DOI) |Machine-readable docs | Systematic review | Scripting | Compatibility | Dockers-Virtual Environments-Pinning

**Goal:** In this tutorial students will create a template of standard documentation, which they can use later in their carreer. Furthermore students know how to perform a systematic review.

**Students Preparation:** See lecture preparation

**Grading:** The documents will be handed in by forking a Github page. Here students create a folder with their own name, and add their documents in a document structure. In a README. MD, students explain their structure briefly. This will be graded with a pass/fail
After uploading their documents they will merge their fork with the original by a pull requist. Note: Merging and forking, must be done in a specific order of students.

**The Idea:** 
+ **Create documents and a folder structure**
  + Create a folder on your computer and call it, STUDENTNUMBER_WEEK4
  + The goal of this exercise is to create a folder structure inside this new folder
  + Create a folder structure as described in box 1 above. Not every step or document in this list can be made, instead create a dummy document. This exercise is to practise good practises and to see all the steps. For example, 3.collaboration.b, can be an empty to-do list in the form of an MD file. When this folder structure is on a repository, one can fork and pull this to-do document to make changes. 
Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, et al. (2017) Good enough practices in scientific computing. PLOS Computational Biology 13(6): e1005510. https://doi.org/10.1371/journal.pcbi.1005510 
  + After you are done, you can fork the repository of this course, and upload your folder with the correct name. Now it is ready to be merged in the main, by a pull request. This process needs to be coordinated by a TA. 
  + A impression of a folder structure with standard documents, (!Not complete!): 
![image](https://user-images.githubusercontent.com/93695286/223513683-add45690-4eee-4d03-84bd-935faeb173f6.png)



+ **Prepare a systematic review**
  + Students pick a topic which is relevant for them. Then they write down a search query in google scholar. See: https://guides.library.ucsc.edu/c.php?g=745384&p=5361954
  + Download the first 100 articles in your search queries and store them in Zotero by entering DOI's
  + Download ASReview: https://asreview.nl/
  + Upload The zotero database in ASReview and scan 6 articles on relevance based on their abstract.
  + After that, ASReview will generate an order of articles for you. Go through these ordered articles and stop when articles are not relevant anymore.
  + The resulting articles, i.e., the first few, will be the articles you will study in a systematic review.

+ **Create a python environment**
    + Fork the course repository
    + Create a folder called, STUDENTNUMBER_ENV
    + Create a python environment, where you install a package. For example, PYQT5 can be installed. This is a package, used often in experimental physics and is never installed as a standard. 
    + Create a new python file in this environment and Create something simple with it. Want to do something more advanced? See for example: https://realpython.com/python-pyqt-gui-calculator/ 
    + Or use https://www.youtube.com/watch?v=FVpho_UiDAY to build a GUI
    + Upload your environment and your code at the forked repository. 
    + Finish with a pull request.

## Information Sources / Bibliography
Best practises
+ Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, et al. (2017) Good enough practices in scientific computing. PLOS Computational Biology 13(6): e1005510. https://doi.org/10.1371/journal.pcbi.1005510

Version control
+ Blischak JD, Davenport ER, Wilson G (2016) A Quick Introduction to Version Control with Git and GitHub. PLOS Computational Biology 12(1): e1004668. https://doi.org/10.1371/journal.pcbi.1004668 

GDPR
+ https://www.surf.nl/en/general-data-protection-regulation-gdpr 

Systematic review
+ https://asreview.nl/

