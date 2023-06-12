# Course Development Week 5
Lecture plan for Week 5 of the OS4P: Open Science Course for physics students at graduate level.

last updated: 05/06/2023

Responsible author: Sanli @sanlifaez

contributors: 
- Hendrik Snijder @hendelhendel
- Erik van Sebille @erikvansebille

Open tasks @SanliFaez 
+ Pick one lecture among the available option
+ Write down the reproducibility exercise
+ Specify the requirements for the open hardware measurement project

## Goal: open design and open hardware; prototyping? 
After this week, one is familier witht he concept of openscience in hardware development. Students get familiar with finding open hardware recipies and know how to contribute to them. After the lecture students can explain in a discussion what challenges open hardware can solve and what socio-economic issues are involved. 


![Frontpage](LINK TO PICTURE)
![image](https://user-images.githubusercontent.com/93695286/221529025-cc8a838e-f1d7-4a2d-b538-8bc0a939a538.png)



## Keywords

|**New Concepts**|**Familiar Concepts**|
|----------------|---------------|
|Scientific design environments||
|Open protocols||
|Microcontrollers||
|Human-computer interface||
|Automation and bots||
|Remote labs||
|Materials-resources-constraints||
|Defense and national security ||
|Maintenance||
|Prototyping||
||

## Lecture: Week 5 
**Topics in lecture**

Scientific design environments| Open protocols|Human-computer interface|Automation and bots|Remote labs|Materials-resources-constraints|Defense and national security |Maintenance|Prototyping
### Lecture preparation
+ Watch the Ted talk by Nathan Seidle on Open hardware https://www.youtube.com/watch?v=Rfu_MKgu2Ik 
+ Watch and read News about Remote Labs https://www.youtube.com/watch?v=8Xo1noxm4R0 (Omroep brabant) and https://www.theguardian.com/science/2022/sep/11/cloud-labs-and-remote-research-arent-the-future-of-science-theyre-here  (Guardian)
+ Extra: https://www.youtube.com/watch?v=iF5-aDJOr6U (virtual lab)
+ Answer the question: How does the future of hardware look like in 2030, 2040 and 2050? Answer in 5 keywords. So the student will bring 3 times 5 keywords to the lecture.
+ Answer the question: What role can open hardware take in society?
+ Resource the game: A little game similar to a sudoku, where students have to solve a recourses problem. Must be developed and it must not be too hard! The answer should hint to design devices made from widely available materials.
+ Extra (Measurement failures): https://www.nature.com/articles/nature.2012.10249 
+ Extra (Measurement failures): https://www.rug.nl/about-ug/latest-news/press-information/scientists-in-focus/romeijnneutrinoen.pdf


### Lecture format
The lecture contains 2 parts. Both answer a specific question related to open hardware and its possible role in society. In preperation, the students have already thought about these questions by reading the materials above. 

What does the future of hardware look like? (30 min) 


At the beginning of the lecture, a word cloud is created with the answers of the students for 2030, 2040 and 2050. Then the lecture starts covering the topics: Scientific design environments, open protocols and human-computer interfaces, Automation and bots, remote labs, prototyping. In the above question will be answered by the teacher, and this will be compared with the student input. 


**Part 2** What physical and political constrains and advances is open hardware facing? (30min)
 
recourse the game will be showed and the correct answer will be displayed together with a quote of Sanli Faez. “Sanli: The difference between open hardware and open software is that copying code does not require extra materials, while reproducing hardware is material dependent. So one should consider the choice of materials and access to it if real openness is a goal.””
The rest of the lecture teaches the students on: Materials-resource-constraints, Defence and national security, Maintenance.


## Tutorial: Week 5
**Topics in tutorial:**

Microcontrollers: a chip where small buttons, Light LED’s, .. can be connected to, to create a computing circuit. Use an assemblage language and an assembler


### Tutorial format
**Tutorial Goal**
Goal of this tutorial is to use open hardware resources, to create a piece of hardware and do a sensing experiment with it. Another goal of this tutorial is that students understand that every individual device, however similar, act different. A connection with Big Science can be made here. 

**Assignment objective**
Some possible hardware devices and measurements ideas are presented below. It is by the course leaders to choose a project, or come up with a similar project. Due to time, things need to be pre-fabricated. A possibility is to do that in @lily’sprotolab, where things such as 3D printing and microcontrollers, can be prepared, such that the students can focus on the assemblage and measurement. 
It can be wise to combine different projects from below. For example, option 3 and option 4 can be combined. 
Furhtermore, students can do their experiments in a specific order, where they realy on eachother's measurement results. If this is done in two groups with similar devices, the final results can be compared in order to show, that even a different procedure can give different results. A connection with bigscience can be made here.

+ **Option 1:** Build a Powerbank and perform and measure it’s impedance. This can be done with typical lab devices such as a potentiostat. If there is plenty of time one such equipment on their own potentiostat. 
  + Powerbank: https://www.printables.com/model/391695-wip-power-bank-3s2p-6-in-a-row-18650-connector-cas 
  + Potentiostat: https://www.hardware-x.com/article/S2468-0672(20)30072-9/fulltext 
  + Potentiostat: https://www.hardware-x.com/article/S2468-0672(22)00035-9/fulltext#secst090 
  + Potentiostat: https://iorodeo.com/products/rodeostat 

+ **Option 2** Thermometer. 
assemblage thermometer: Infrared thermometer (35 dollar): https://reader.elsevier.com/reader/sd/pii/S2468067220300778?token=67B0158CF8096F48C79436B2C0CECE90DA182F4C3F00B55B4D595529B5F202CCFF34D74EB1E374C79E6F7CFED060BBCC&originRegion=eu-west-1&originCreation=20230223121938 
Measure average temp of students


+ **Pption 3** Air quality measurement:
Assemblage of : https://www.airgradient.com/open-airgradient/instructions/diy/ 
Measure the Airquality and compare it with https://aqicn.org/city/utrecht/ 

+ **Option 4**
Pick an experiment of Phyphox which can be done on a smartphone. Let students peform this expirment, and let them compare the results with some simple statistics. 
As an example, students can measure the speed of sound (https://phyphox.org/experiment/speed-of-sound/) to calculate the outside temperature of the air with. To learn that every device is different, students can compare their results and can compare it with offical weather data.
https://phyphox.org/experiment/

+ **Option 5** Any project with a raspberry pi pico and micro-python to make a little device, to do a measurement. 
+ **Option 6** Choose another Open hardware device and assemblage it during the tutorial in order to perform a measurement.

## Inspiration for future projects
+ https://www.printables.com/model/394957-mount-for-arduino-nano 
+ Potentiostat: https://www.hardware-x.com/article/S2468-0672(20)30072-9/fulltext 
+ potentiostat: https://www.hardware-x.com/article/S2468-0672(22)00035-9/fulltext#secst090 
+ https://codingcat.nl/book/thermal_expansion.html 
+ https://www.printables.com/education/288422-elektromotor 
+ https://www.hardware-x.com/article/S2468-0672(22)00133-X/fulltext 
+ Light weight drone to use in measure in hazard areas : https://www.hardware-x.com/action/showPdf?pii=S2468-0672%2822%2900058-X 
+ USV vehicle to measure water qualit: https://www.hardware-x.com/article/S2468-0672(19)30036-7/fulltext  
+ GPS, electrical conductivity and temperature sensing device: https://www.hardware-x.com/article/S2468-0672(22)00126-2/fulltext 
+ MOdular light source: https://www.hardware-x.com/article/S2468-0672(22)00130-4/fulltext 


+ Experimental design course UU, for students how are interested to build more open hardware devices.: https://osiris.uu.nl/osiris_student_uuprd/OnderwijsCatalogusSelect.do?selectie=cursus&cursus=NS-EX422M&collegejaar=2020&taal=nl 
+ Open challanges on Jogl: https://jogl.io/ 
+ Fablab: https://waag.org/en/lab/fablab/ 
+ Future labs Maybe for week 2?: https://ddw.nl/en/programme/7942/waag-talks-start-making-sense 
+ Future labs: https://waag.org/en/project/ 
+ Week 3(?) https://waag.org/nl/article/hollandse-luchten-sensorkit/ 

Open hardware makers
+ https://twitter.com/openHWmakers 
+ https://www.youtube.com/@openHWmakers 
+ https://openhardware.space/ 


## Information Sources / Bibliography
Scientific design environments, Open protocols, Microcontrollers, Human-computer interface, Automation and bots, Remote labs, Materials-resources-constraints, Defense and national security, Maintenance, Prototyping

Human-computer interface
+ https://www.sciencedirect.com/science/article/pii/B0080430767043333 
+ https://www.sciencedirect.com/science/article/pii/B9780123742674000082 
+ https://www.sciencedirect.com/science/article/pii/B9780123875822500411 
+ https://www.sciencedirect.com/science/article/pii/B9780128161760000387 
+ https://www.sciencedirect.com/science/article/pii/B9780128161760000387 
+ https://www.sciencedirect.com/science/article/abs/pii/S0065245810800075  

micro-controlers (Rasberry pi )
+ https://www.seeedstudio.com/blog/2021/03/26/10-raspberry-pi-pico-projects/
+ https://elektronicavoorjou.nl/product/uitgebreide-kit-rpi-pico/?gclid=Cj0KCQiA_P6dBhD1ARIsAAGI7HAQVck4jLfjT6BMmpt6Oo8pIBRfXfyF462kJCdKEXirv8PycbayX0YaAnRcEALw_wcB
+ Rasberry Pi projects: https://www.magpi.nl/magazine/2023/28 

Journal: HardwareX (=open acces hardware)
+ Open hardware: https://en.wikipedia.org/wiki/List_of_open-source_hardware 
+ Remote Laboratory:
+ https://remotelaboratory.com/remote-laboratories/what-are-remote-laboratories/ 

Open technology course:
+ https://free-and-open-technologies.github.io/ 

Design environment:
+ https://all3dp.com/2/best-open-source-cad-software/ 
+ https://www.qcad.org/en/ 
+ 2d https://www.qcad.org/en/ 
+ 3d: OpenSCAD https://openscad.org/ 
+ PCB design: https://circuitmaker.com/ 

Open protocols: (Software focus) 
+ https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:the-internet/xcae6f4a7ff015e7d:developing-open-protocols/a/open-standards-and-protocols 
+ https://www.open.edu/openlearncreate/mod/oucontent/view.php?id=129583&printable=1 


Materials-resources-constraints
+ matrials: https://openmaterialsdb.se/ 
+ Battery archive: https://www.batteryarchive.org/resources.html 
+ Material Challanges and how to solve them in EU: https://www.wetenschappelijkbureaugroenlinks.nl/metals-for-europe 
+ Economics: https://www.bol.com/nl/nl/f/less-is-more/9200000128080503/ 
+ Economics: https://www.bol.com/nl/nl/p/doughnut-economics/9200000083131123/?Referrer=ADVNLGOO002008O-G-139188994260-S-1926802725980-9200000083131123&gclid=Cj0KCQiA3eGfBhCeARIsACpJNU-UrHw7bwYUu5JB9y7D6iHpi8i0jKCj3gZZebZxQoLtZIHYPUVy19MaAv1kEALw_wcB 
+ Economics: http://www.rutgerhoekstra.com/replacing-gdp-by-2030/ 
+ https://link.springer.com/article/10.1007/s10368-017-0385-3 
+ tps://link.springer.com/article/10.1007/s10368-011-0195-y 
+ International Monetary Fund on material recourses and economy: https://www.imf.org/en/Publications/WP/Issues/2022/02/15/Supply-Bottlenecks-Where-Why-How-Much-and-What-Next-513188 
+ Fair battery project: https://github.com/SanliFaez/FAIR-Battery
