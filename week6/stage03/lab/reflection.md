The hardest modelling decision was conceptualising how the clinic's business functions translated into classes and how those classes should interact with one another. While identifying the main entities such as Patient, Practitioner, and Appointment was relatively straightforward from the requirements, determining their responsibilities and relationships was more challenging. I found it difficult to decide which class should own what particular data and behaviours, and how information should flow between objects. This required repeatedly referring to the requirements to ensure that the model reflected the clinic's real-world processes. Fortunately, I did Systems Analysis and Design last semester! 

 

AI-assisted suggestions sometimes over-designed the solution by introducing additional complexity beyond what was required by the scenario. In many cases, extra classes, relationships, or features were proposed that were not directly supported by the requirements. However, this was partly due to the way I prompted CoPilot. This experience highlighted the importance of critically evaluating AI-generated suggestions rather than accepting them without review. 

 

The evidence supporting my final modelling choices was the degree to which each class's attributes and methods could be directly traced back to the documented requirements. I selected designs that provided the simplest solution while still satisfying the stated functional requirements and maintaining clear responsibilities between classes. 