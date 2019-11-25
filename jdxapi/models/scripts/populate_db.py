from jdxapi.models import Framework, FrameworkType
from jdxapi.app import DB

competency_framework_type = FrameworkType(
    framework_type = "competency"
)

occupation_framework_type = FrameworkType(
    framework_type = "occupation"
)

industry_framework_type = FrameworkType(
    framework_type = "industry"
)

DB.session.add_all([
    competency_framework_type,
    occupation_framework_type,
    industry_framework_type
])
DB.session.commit()


DB.session.add_all([
    Framework(
        # framework_id = UUID('24a46ca3-d9f0-5121-9f81-c2bcf9bd4311'),
        framework_type = competency_framework_type,
        framework_name = 'AARC Respiratory Care',    
    ),
    Framework(
        # framework_id = UUID('9cfd2436-0483-5def-9da5-bd22e2fe6272'),
        framework_type = competency_framework_type,
        framework_name = 'Automation ClearingHouse Model',    
    ),
    Framework(
        # framework_id = UUID('aa4a678f-8b23-5fc2-b443-bed20a9dd635'),
        framework_type = competency_framework_type,
        framework_name = 'Comerical Construction ClearingHouse Model',    
    ),
    Framework(
        # framework_id = UUID('395265fe-e59e-5817-a0cf-fb7ec9f9efbc'),
        framework_type = competency_framework_type,
        framework_name = 'Cybersecurity ClearingHouse Model',    
    ),
    Framework(
        # framework_id = UUID('5d52c92e-8be3-561d-8a1f-69004d843485'),
        framework_type = competency_framework_type,
        framework_name = 'Energy Generation, Transmission and Distribution Competency Model',    
    ),
    Framework(
        # framework_id = UUID('efb9d2f3-9528-5fb3-8edb-0299b54336bf'),
        framework_type = competency_framework_type,
        framework_name = 'ESCO Skills and Competencies',    
    ),
    Framework(
        # framework_id = UUID('184d3df5-c955-550a-b139-aac601565de3'),
        framework_type = competency_framework_type,
        framework_name = 'Surgical Technologist Certifying Examination Content',    
    ),
    Framework(
        # framework_id = UUID('fc7e57a6-8a48-5ec1-bfbf-9ecd0f5ebacf'),
        framework_type = competency_framework_type,
        framework_name = 'Multipurpose Occupational Systems Analysis Inventory - Close-Ended (MOSAIC) Competencies',    
    ),
    Framework(
        # framework_id = UUID('b6e5d991-0f18-54ae-8198-bde671ecdbf1'),
        framework_type = competency_framework_type,
        framework_name = 'Retail Competency Model',    
    ),
    Framework(
        # framework_id = UUID('34224458-ca06-5832-8367-351855408a47'),
        framework_type = competency_framework_type,
        framework_name = 'Registered Respiratory Therapist',    
    ),
    Framework(
        # framework_id = UUID('6c1d16ae-2779-5703-92ef-99782eba84bc'),
        framework_type = competency_framework_type,
        framework_name = 'Transportation, Distribution, and Logistics Competency Model',    
    ),
    Framework(
        # framework_id="e1499ffb-7c8f-575b-ae3e-3662cd186130"
        framework_type = competency_framework_type,
        framework_name ="Long-term Care, Supports, and Services Competency Model",    
    ),
    Framework(
        # framework_id: "54a26a56-811b-5588-89c1-9e64f18276d1"
        framework_type = competency_framework_type,
        framework_name ="NIST NICE Cybersecurity Framework",    
    ),
    Framework(
        # framework_id = "50d622c0-478f-5220-b5d2-1c93c0e4ff38"
        framework_type = competency_framework_type,
        framework_name = "NIMS DUTIES AND STANDARDS FOR INDUSTRIAL MAINTENANCE TECHNICIANS",    
    ),
    Framework(
        # framework_id = "1da0d628-0b1c-5516-9f64-99ceeb32a9d5"
        framework_type = competency_framework_type,
        framework_name = "NCEES Principles and Practice of Engineering Examination",    
    ),
    Framework(
        # framework_id = "af40accf-95fa-5b50-828f-a7e2477e3d07"
        framework_type = competency_framework_type,
        framework_name = "MCSD App Builder Skill lists",    
    ),
    Framework(
        # framework_id = "841fd4a7-611a-5c7f-9d49-74dd87b1ac75"
        framework_type = competency_framework_type,
        framework_name = "Nursing Critical Care/Intensive Care Skills",    
    ),
    Framework(
        # framework_id = "78ab8c32-80d1-56a6-b955-a4bbcb92143c"
        framework_type = competency_framework_type,
        framework_name = "The Community Roundtable Community Manager Skills - Business Partnerships",    
    ),
    Framework(
        # framework_id = "41fd1868-1964-5219-92f4-2777e794ff85"
        framework_type = competency_framework_type,
        framework_name = "Blue Prism",    
    ),
    Framework(
        # framework_id = "39d10a55-a1c4-508d-ab3f-55ee51625c3f"
        framework_type = competency_framework_type,
        framework_name = "ONET Knowledge, Skills, Abilities",    
    ),
    Framework(
        # framework_id = "a56bc89c-5da7-5e51-815f-621b9af3f020"
        framework_type = competency_framework_type,
        framework_name = "ONET Software Quality Assurance Engineers and Tester"
    ),
    Framework(
        # framework_id = "bf820ded-fc91-516a-b985-be08fc0bc6f4"
        framework_type = competency_framework_type,
        framework_name = "ONET Computer Systems Engineers/Architects"
    ),
    Framework(
        # framework_id = "d63bc6a8-7a07-5126-a422-43960fe906bf"
        framework_type = competency_framework_type,
        framework_name = "O*NET Construction and Building Inspectors"
    ),
    Framework(
        # framework_id = "7b403943-835b-56c9-9561-e9222ebb18c3"
        framework_type = competency_framework_type,
        framework_name = "O*NET Maintenance and Repair Workers, General"
    ),
    Framework(
        # framework_id: "a324dba2-dc47-54d1-95ed-c57392b6976e"
        framework_type = competency_framework_type,
        framework_name = "Entry Level Software or Application Developer"
    ),
    Framework(
        # framework_id: "e958001a-e1fd-536a-a4ee-3fbcda1f5bd2"
        framework_type = competency_framework_type,
        framework_name = "O*NET Licensed Practical and Licensed Vocational Nurses"
    ),
    Framework(
        # framework_id: "ffd00e0c-e7e7-5b8d-b79b-f810cf72ce0d"
        framework_type = competency_framework_type,
        framework_name = "O*NET Software Developers, Applications"
    ),
    Framework(
        # framework_id: "9c7e8b80-937f-56b3-9397-903e06f80272"
        framework_type = competency_framework_type,
        framework_name = "O*NET Software Developers, Systems Software"
    ),
    Framework(
        # framework_id: "3313cbf0-c3a8-59fa-a567-1c702426a2fa"
        framework_type = competency_framework_type,
        framework_name = "ARDMS Fetal Echocardiography Exam Content Outline"
    ),
    Framework(
        # framework_id: "44a01b50-4628-51e0-b06a-aae3e669d5b8"
        framework_type = competency_framework_type,
        framework_name = "Competency Model Clearinghouse IT Competency Model"
    ),
    Framework(
        # framework_id: "cd546b16-f5c1-55a4-ab02-d210d1f2bb45"
        framework_type = competency_framework_type,
        framework_name = "SEMI Adv Manu Comp Clearinghouse Model + Microelectronics Manu Sector"
    )
])


DB.session.commit()

print(DB.session.query(Framework).all())