# Sugerencia de trabajo

1. Cargar la info del candidato (pueden usar pandas) >> Tabla

`Candidate Education.json`

```json
{
    "degree": "BA/BS",
    "status": "COMPLETED",
    "career": "Mechatronics, Robotics, and Automation Engineering",
}
```     

`Candidate Working Experience.json`

```json
"role": "DevOps Engineer",
"responsibilities": [],
"description": "Working on a customer service AI multi tenant platform."
``` 

2. Definir variable objetivo del job description (Y= Objetivo)

`Job Description.json`
```json
"responsibilities": [
        "Advocate for the use of cutting-edge technology to build intelligent and scalable products.",
        "Act as a technology partner for our clients from inception to completion while architecting reusable front-end systems by understanding their needs and translating requirements into world-class design.",
        "Responsible for delivering high-quality applications.",
        "Act as a relationship builder with direct communication with stakeholders, you will also drive internal initiatives and objectives.",
        "Working on projects that will allow you to develop your skills and gain exposure to multinational brands.",
        "Partner with multidisciplinary teams located across the world (Technical Writing, User Experience, Product Management, and Project Management) to solve challenging problems."
    ],
"type": "FULL-TIME",
"role": "Senior Java Developer ",
"stack": [
        "Java",
        "Python",
        "AWS",
        "Spring boot"
    ]
"description": "We’re looking for a Java Engineer SR to join a global digital services company helping mid-size to Fortune 500 companies build, scale, and deliver high-quality digital products and services.",
"requirements": [
        "Strong Client Management experience.",
        "Hands-on and leadership experience in developing secure and scalable enterprise applications.",
        "5+ years of experience with Java.",
        "2+ years of experience with Java 8, 11,17, Javascript and Python.",
        "Experience with Spring Boot, Core, and Cloud.",
        "Passion and experience building web-based technology products or applications.",
        "Strong notions on the principles of microservices patterns and design patterns.",
        "Knowledge in non-relational databases: DynamoDB and MongoDB.",
        "Advanced English.",
        "Argentina resident."
]
```

3. Para hacer el match les sugiero usar comparacion de texto (Embeddings, Distancias de Texto e.g Jaccard entre otras)

- responsibilities (`Job Description.json`) vs responsibilities (`Candidate Working Experience.json`).
S1= Sugerencia usar embeddings y usar similitud de cosine (0-1)
- description (`Job Description.json`) vs description (`Candidate Working Experience.json`).
S2= Sugerencia usar embeddings y usar similitud de cosine (0-1)
- role (`Job Description.json`) vs role (`Candidate Working Experience.json`).
S3= Sugerencia usar embeddings y usar similitud de cosine (0-1)
- career,responsibilities (`Job Description.json`) vs requirements (`Candidate Working Experience.json`).
S4= Sugerencia usar embeddings y usar similitud de cosine (0-1)

4. Promedio ponderado para indice final de matching

SF = 1/4 (S1+S2+S3+s4)

Min SF =0
Max SF =1
