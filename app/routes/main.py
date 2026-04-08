from flask import Blueprint, render_template, request, send_from_directory, current_app

main_bp = Blueprint("main", __name__)


def get_lang():
    lang = request.args.get("lang", "pt")
    return lang if lang in {"pt", "en"} else "pt"


def tr(lang, pt, en):
    return pt if lang == "pt" else en


@main_bp.route("/")
def index():
    lang = get_lang()
    highlights = [
        {
            "title": tr(lang, "Perfil profissional", "Professional profile"),
            "description": tr(lang,
                "Acesse experiência em IA, ciência de dados, automação, indústria, software e docência em uma visão direta e organizada.",
                "Access experience in AI, data science, automation, industry, software, and teaching in a direct and organized view."),
            "icon": "badge",
        },
        {
            "title": tr(lang, "Projetos e GitHub", "Projects and GitHub"),
            "description": tr(lang,
                "Veja aplicações, repositórios, estudos e entregas técnicas com foco em uso real, clareza e deploy.",
                "Review applications, repositories, studies, and technical deliveries focused on real use, clarity, and deployment."),
            "icon": "deployed_code",
        },
        {
            "title": tr(lang, "Sala de Aula", "Classroom"),
            "description": tr(lang,
                "Abra disciplinas, materiais simulados e trilhas de ensino nas áreas de IA e programação em tempo real.",
                "Open courses, simulated materials, and teaching tracks in AI and real-time programming."),
            "icon": "school",
        },
    ]
    metrics = [
        {"value": tr(lang, "+20 anos", "20+ years"), "label": tr(lang, "trajetória entre indústria, tecnologia e ensino", "career across industry, technology, and teaching")},
        {"value": "PT / EN", "label": tr(lang, "navegação bilíngue", "bilingual navigation")},
        {"value": "Cloud Run", "label": tr(lang, "base pronta para deploy", "deployment-ready foundation")},
        {"value": tr(lang, "CV + GitHub", "CV + GitHub"), "label": tr(lang, "acesso direto ao conteúdo principal", "direct access to core content")},
    ]
    quick_access = [
        {
            "title": tr(lang, "Currículo", "Resume"),
            "description": tr(lang, "Veja experiência, formação, foco técnico e stack.", "Review experience, education, technical focus, and stack."),
            "url": "main.resume",
            "cta": tr(lang, "Abrir currículo", "Open resume"),
        },
        {
            "title": tr(lang, "Projetos", "Projects"),
            "description": tr(lang, "Acesse curadoria técnica e repositórios do GitHub.", "Access technical curation and GitHub repositories."),
            "url": "projects.list_projects",
            "cta": tr(lang, "Abrir projetos", "Open projects"),
        },
        {
            "title": tr(lang, "Sala de Aula", "Classroom"),
            "description": tr(lang, "Abra disciplinas, tópicos e materiais simulados.", "Open courses, topics, and simulated materials."),
            "url": "teaching.teaching_home",
            "cta": tr(lang, "Abrir sala de aula", "Open classroom"),
        },
        {
            "title": "Lab",
            "description": tr(lang, "Consulte demos, protótipos e frentes aplicadas.", "Review demos, prototypes, and applied tracks."),
            "url": "main.lab",
            "cta": tr(lang, "Abrir lab", "Open lab"),
        },
    ]
    classroom_cards = [
        {
            "slug": "disciplina-1",
            "title": tr(lang, "Disciplina 1", "Course 1"),
            "subtitle": tr(lang, "Inteligência Artificial", "Artificial Intelligence"),
            "description": tr(lang,
                "Fundamentos, modelagem, avaliação de modelos e aplicações orientadas a problema.",
                "Foundations, modeling, model evaluation, and problem-driven applications."),
            "meta": [tr(lang, "Modelagem", "Modeling"), tr(lang, "Métricas", "Metrics"), tr(lang, "Aplicações", "Applications")],
        },
        {
            "slug": "disciplina-2",
            "title": tr(lang, "Disciplina 2", "Course 2"),
            "subtitle": tr(lang, "Programação em Tempo Real", "Real-Time Programming"),
            "description": tr(lang,
                "ESP32, tarefas concorrentes, temporização, periféricos e RTOS.",
                "ESP32, concurrent tasks, timing, peripherals, and RTOS."),
            "meta": ["ESP32", "RTOS", tr(lang, "Laboratório", "Lab")],
        },
        {
            "slug": "disciplina-3",
            "title": tr(lang, "Disciplina 3", "Course 3"),
            "subtitle": tr(lang, "Introdução à IA", "Introduction to AI"),
            "description": tr(lang,
                "História, paradigmas, agentes, ética e leitura crítica de casos de uso.",
                "History, paradigms, agents, ethics, and critical reading of use cases."),
            "meta": [tr(lang, "Fundamentos", "Foundations"), tr(lang, "Conceitos", "Concepts"), tr(lang, "Ética", "Ethics")],
        },
    ]
    about_lines = [
        tr(lang, "Acesse o currículo para ver experiência profissional, formação e stack técnica.", "Access the resume to review professional experience, education, and technical stack."),
        tr(lang, "Abra os projetos para ver repositórios, aplicações e frentes de desenvolvimento.", "Open projects to review repositories, applications, and development tracks."),
        tr(lang, "Use a Sala de Aula para acessar disciplinas e conteúdo demonstrativo.", "Use the Classroom to access courses and demonstrative content."),
    ]
    pillars = [
        tr(lang, "Conteúdo organizado para recrutadores, clientes, parceiros, alunos e equipes técnicas.", "Content organized for recruiters, clients, partners, students, and technical teams."),
        tr(lang, "Navegação direta para currículo, GitHub, disciplinas, laboratório e contato.", "Direct navigation to resume, GitHub, courses, lab, and contact."),
        tr(lang, "Estrutura leve para publicação em Flask com deploy em Google Cloud Run.", "Lightweight structure for Flask publishing with Google Cloud Run deployment."),
    ]
    spotlight = [
        tr(lang, "Experiência em machine learning, ciência de dados, analytics, MLOps e produtos analíticos.", "Experience in machine learning, data science, analytics, MLOps, and analytical products."),
        tr(lang, "Experiência industrial em manutenção, automação, produção, planejamento e confiabilidade.", "Industrial experience in maintenance, automation, production, planning, and reliability."),
        tr(lang, "Atuação acadêmica em IA, lógica, estatística, pesquisa operacional e sistemas embarcados.", "Academic work in AI, logic, statistics, operations research, and embedded systems."),
    ]
    leadership_tracks = [
        tr(lang, "Atuação entre contexto executivo, técnico e didático com comunicação clara.", "Work across executive, technical, and teaching contexts with clear communication."),
        tr(lang, "Capacidade de transformar problemas operacionais em soluções digitais e analíticas.", "Ability to turn operational problems into digital and analytical solutions."),
        tr(lang, "Base quantitativa e de engenharia aplicada para produtos, processos e aprendizado técnico.", "Quantitative and applied engineering background for products, processes, and technical learning."),
    ]
    hero = {
        "chip": tr(lang, "Plataforma pessoal e profissional", "Personal and professional platform"),
        "title": tr(lang, "TekForge é um hub de tecnologia que reúne perfil profissional, projetos, materiais de ensino e aplicações.", "TekForge is a technology hub that brings together professional profile, projects, teaching materials, and applications."),
        "subtitle": tr(lang, "Acesse currículo, GitHub, disciplinas e aplicações em uma plataforma direta, bilíngue e pronta para deploy.", "Access resume, GitHub, courses, and applications in a direct, bilingual platform ready for deployment."),
        "primary": tr(lang, "Abrir projetos", "Open projects"),
        "secondary": tr(lang, "Abrir currículo", "Open resume"),
    }
    sections = {
        "areas_title": tr(lang, "Acesso principal", "Main access"),
        "areas_subtitle": tr(lang, "Use estes blocos para chegar rapidamente ao conteúdo central da plataforma.", "Use these blocks to reach the platform's core content quickly."),
        "classroom_title": tr(lang, "Disciplinas", "Courses"),
        "classroom_subtitle": tr(lang, "Abra disciplinas em cards com acesso direto ao conteúdo.", "Open courses in cards with direct access to content."),
        "pillars_title": tr(lang, "Como usar a plataforma", "How to use the platform"),
        "pillars_subtitle": tr(lang, "Veja o que está disponível e use o menu para navegar sem fricção.", "See what is available and use the menu to navigate without friction."),
        "tracks_title": tr(lang, "Leitura rápida do perfil", "Quick profile read"),
        "tracks_subtitle": tr(lang, "Use estes blocos para entender o escopo de atuação de forma objetiva.", "Use these blocks to understand the scope of work objectively."),
        "about_title": tr(lang, "Acesso rápido", "Quick access"),
        "about_subtitle": tr(lang, "Entre diretamente nas áreas mais usadas do site.", "Go directly into the most used areas of the site."),
    }
    return render_template(
        'index.html', lang=lang, hero=hero, highlights=highlights, metrics=metrics,
        classroom_cards=classroom_cards, pillars=pillars, spotlight=spotlight,
        leadership_tracks=leadership_tracks, sections=sections, about_lines=about_lines,
        quick_access=quick_access,
    )


@main_bp.route('/resume')
def resume():
    lang = get_lang()
    professional_summary = tr(lang,
        "Engenheiro e Cientista de Dados com trajetória construída entre indústria, manutenção preditiva, automação industrial, engenharia de processos, machine learning, analytics, software e ensino superior. Acesse nesta página uma visão consolidada da experiência profissional, da formação acadêmica e das especialidades técnicas que estruturam a atuação atual.",
        "Engineer and Data Scientist with a career built across industry, predictive maintenance, industrial automation, process engineering, machine learning, analytics, software, and higher education. Access on this page a consolidated view of professional experience, academic background, and technical specialties that support current work.")
    resume_stats = [
        {"value": tr(lang, "+20 anos", "20+ years"), "label": tr(lang, "experiência combinada", "combined experience")},
        {"value": tr(lang, "8+", "8+"), "label": tr(lang, "disciplinas lecionadas", "taught subjects")},
        {"value": tr(lang, "IA + Indústria", "AI + Industry"), "label": tr(lang, "interseção principal", "main intersection")},
        {"value": "PT / EN", "label": tr(lang, "navegação bilíngue", "bilingual navigation")},
    ]
    experience_groups = [
        {
            "title": tr(lang, "IA, dados e produtos analíticos", "AI, data, and analytical products"),
            "entries": [
                {
                    "role": tr(lang, "Especialista em Machine Learning", "Machine Learning Specialist"),
                    "org": "act digital",
                    "period": tr(lang, "nov/2025 · atual", "Nov/2025 · present"),
                    "description": tr(lang, "Atuação em soluções de machine learning, analytics e produtos de dados com foco em clareza técnica, deploy e utilidade para negócio.", "Works on machine learning solutions, analytics, and data products focused on technical clarity, deployment, and business utility."),
                },
                {
                    "role": tr(lang, "Cientista de Dados Sênior", "Senior Data Scientist"),
                    "org": "Zup Innovation",
                    "period": tr(lang, "jan/2024 · fev/2024", "Jan/2024 · Feb/2024"),
                    "description": tr(lang, "Atuação em ciência de dados sênior em contexto bancário, apoiando análises e entregas orientadas a negócio.", "Worked as a senior data scientist in a banking context, supporting business-oriented analytics and deliveries."),
                },
                {
                    "role": tr(lang, "Cientista de Dados Sênior", "Senior Data Scientist"),
                    "org": "Neon",
                    "period": tr(lang, "abr/2022 · out/2023", "Apr/2022 · Oct/2023"),
                    "description": tr(lang, "Conduziu análises avançadas, modelagem estatística, clusterização, experimentação, Media Mix Modelling, procedimentos de mensuração e aplicações com pySpark.", "Led advanced analytics, statistical modeling, clustering, experimentation, media mix modeling, measurement procedures, and pySpark-based applications."),
                },
                {
                    "role": tr(lang, "Engenheiro de Machine Learning", "Machine Learning Engineer"),
                    "org": "Tek Bunker Soluções Tecnológicas",
                    "period": tr(lang, "mar/2019 · abr/2022", "Mar/2019 · Apr/2022"),
                    "description": tr(lang, "Desenvolveu projetos para a indústria farmacêutica com visão computacional, previsão de demanda, otimização de processos e manutenção preditiva baseada em sinais e aprendizado profundo.", "Developed projects for the pharmaceutical industry using computer vision, demand forecasting, process optimization, and predictive maintenance based on signals and deep learning."),
                },
            ],
        },
        {
            "title": tr(lang, "Indústria, manutenção e automação", "Industry, maintenance, and automation"),
            "entries": [
                {
                    "role": tr(lang, "Profissional Sênior de Manutenção", "Maintenance Senior Professional"),
                    "org": "Novo Nordisk",
                    "period": tr(lang, "fev/2024 · out/2025", "Feb/2024 · Oct/2025"),
                    "description": tr(lang, "Atuação com validação de sistemas e equipamentos industriais, automação, robótica, manutenção preditiva, análise de dados industriais, formação de equipes e projetos de melhoria contínua em ambiente farmacêutico.", "Worked with industrial system and equipment validation, automation, robotics, predictive maintenance, industrial data analysis, team training, and continuous improvement projects in a pharmaceutical environment."),
                },
                {
                    "role": tr(lang, "Facilities Manager", "Facilities Manager"),
                    "org": "Nestlé",
                    "period": tr(lang, "nov/2011 · set/2012", "Nov/2011 · Sep/2012"),
                    "description": tr(lang, "Gestão de processos de facilities e contratos de outsourcing, com responsabilidade sobre manutenção, cleaning, catering e security.", "Managed facilities processes and outsourcing contracts, with responsibility for maintenance, cleaning, catering, and security."),
                },
                {
                    "role": tr(lang, "Supervisor de Planejamento Industrial", "Industrial Planning Supervisor"),
                    "org": "Indumetal Estruturas Metálicas",
                    "period": tr(lang, "jun/2009 · jun/2011", "Jun/2009 · Jun/2011"),
                    "description": tr(lang, "Supervisão de planejamento, logística, projetos, planejamento e controle da produção e obras.", "Oversaw planning, logistics, projects, and production and construction control."),
                },
                {
                    "role": tr(lang, "Técnico de Planejamento de Manutenção", "Maintenance Planning Technician"),
                    "org": "Novo Nordisk",
                    "period": tr(lang, "set/2005 · fev/2009", "Sep/2005 · Feb/2009"),
                    "description": tr(lang, "Planejamento de manutenção, elaboração de planos, controle de ordens e atuação como super-user SAP PM.", "Handled maintenance planning, maintenance plan definition, work order control, and SAP PM super-user responsibilities."),
                },
                {
                    "role": tr(lang, "Projetista de orçamentos", "Budget Design Specialist"),
                    "org": "Cometal Estruturas Metálicas",
                    "period": tr(lang, "fev/2004 · set/2005", "Feb/2004 · Sep/2005"),
                    "description": tr(lang, "Levantamentos técnicos, composição de custos, logística, propostas e memoriais para obras em estruturas metálicas.", "Prepared technical takeoffs, cost composition, logistics, proposals, and technical descriptions for steel structure projects."),
                },
                {
                    "role": tr(lang, "Projetista", "Designer"),
                    "org": "Net Service Consultoria",
                    "period": tr(lang, "fev/2002 · dez/2003", "Feb/2002 · Dec/2003"),
                    "description": tr(lang, "Atuação inicial em projeto técnico, leitura de demanda e apoio à execução de entregas técnicas.", "Early work in technical design, demand interpretation, and support for technical deliveries."),
                },
            ],
        },
        {
            "title": tr(lang, "Docência e formação técnica", "Teaching and technical education"),
            "entries": [
                {
                    "role": tr(lang, "Professor universitário", "University Professor"),
                    "org": "UNIFIPMoc",
                    "period": tr(lang, "fev/2026 · atual", "Feb/2026 · present"),
                    "description": tr(lang, "Responsável por Inteligência Artificial, Introdução à IA, Programação em Tempo Real e Lógica Computacional. Também atua na mentoria do grupo acadêmico G.A.I.A.", "Teaches Artificial Intelligence, Introduction to AI, Real-Time Programming, and Computational Logic. Also mentors the G.A.I.A academic group."),
                },
                {
                    "role": tr(lang, "Professor adjunto", "Adjunct Professor"),
                    "org": "UNIFIPMoc",
                    "period": tr(lang, "jun/2012 · dez/2022", "Jun/2012 · Dec/2022"),
                    "description": tr(lang, "Atuação em Engenharia Mecatrônica, Engenharia de Computação e Administração, com disciplinas em algoritmos, estatística aplicada, automação, inteligência computacional, cálculo numérico, pesquisa operacional e otimização.", "Worked across Mechatronics Engineering, Computer Engineering, and Business Administration, teaching algorithms, applied statistics, automation, computational intelligence, numerical methods, operations research, and optimization."),
                },
            ],
        },
    ]
    education = [
        {"title": tr(lang, "Master of Science em Inteligência Artificial e Otimização", "Master of Science in Artificial Intelligence and Optimization"), "description": tr(lang, "Universidade Estadual de Montes Claros · 2015–2017", "State University of Montes Claros · 2015–2017")},
        {"title": tr(lang, "Especialização em Engenharia de Produção", "Specialization in Production Engineering"), "description": tr(lang, "UNIFIPMoc · 2011–2012", "UNIFIPMoc · 2011–2012")},
        {"title": tr(lang, "Bacharelado em Engenharia de Produção", "Bachelor's degree in Production Engineering"), "description": tr(lang, "UNIFIPMoc · 2007–2011", "UNIFIPMoc · 2007–2011")},
        {"title": tr(lang, "Técnico em Automação Industrial", "Industrial Automation Technician"), "description": tr(lang, "FACIT · 1999–2000", "FACIT · 1999–2000")},
    ]
    teaching_disciplines = [
        tr(lang, "Inteligência Artificial", "Artificial Intelligence"),
        tr(lang, "Introdução à Inteligência Artificial", "Introduction to Artificial Intelligence"),
        tr(lang, "Programação em Tempo Real", "Real-Time Programming"),
        tr(lang, "Lógica Computacional", "Computational Logic"),
        tr(lang, "Pesquisa Operacional", "Operations Research"),
        tr(lang, "Estatística", "Statistics"),
        tr(lang, "Controle e Sistemas", "Control and Systems"),
        tr(lang, "Sistemas Embarcados", "Embedded Systems"),
    ]
    focus_areas = [
        {"title": "Machine Learning & MLOps", "description": tr(lang, "Modelagem, avaliação, deploy, monitoramento e aplicações com foco em uso real.", "Modeling, evaluation, deployment, monitoring, and applications focused on real use.")},
        {"title": tr(lang, "Ciência de Dados e Experimentação", "Data Science and Experimentation"), "description": tr(lang, "Análise avançada, modelagem estatística, clusterização, mensuração e experimentos.", "Advanced analytics, statistical modeling, clustering, measurement, and experiments.")},
        {"title": tr(lang, "Indústria e Automação", "Industry and Automation"), "description": tr(lang, "Manutenção, confiabilidade, automação, robótica, validação e melhoria contínua.", "Maintenance, reliability, automation, robotics, validation, and continuous improvement.")},
        {"title": tr(lang, "Educação Tecnológica", "Technology Education"), "description": tr(lang, "Estruturação de conteúdo técnico, mentoria e comunicação clara para ensino superior.", "Technical content structuring, mentoring, and clear communication for higher education.")},
    ]
    stack_groups = [
        {"title": tr(lang, "IA, dados e engenharia analítica", "AI, data, and analytical engineering"), "items": ["Python", "Machine Learning", "MLOps", "PySpark", "Experimentation", "Statistics", "Optimization", "Computer Vision"]},
        {"title": tr(lang, "Software, cloud e aplicações", "Software, cloud, and applications"), "items": ["Flask", "Dash", "Streamlit", "APIs", "Google Cloud", "Cloud Run", "Docker", "GitHub"]},
        {"title": tr(lang, "Indústria e automação", "Industry and automation"), "items": [tr(lang, "Manutenção Preditiva", "Predictive Maintenance"), tr(lang, "Automação Industrial", "Industrial Automation"), "SAP PM", tr(lang, "Validação de Sistemas", "System Validation"), "Robotics", tr(lang, "Planejamento de Produção", "Production Planning")]},
        {"title": tr(lang, "Embarcados e laboratório", "Embedded systems and lab"), "items": ["ESP32", "RTOS", "IoT", tr(lang, "Sistemas Embarcados", "Embedded Systems"), tr(lang, "Sensores e Atuadores", "Sensors and Actuators"), tr(lang, "Prototipação", "Prototyping")]},
    ]
    achievements = [
        tr(lang, "Conecta experiência industrial com construção de soluções em IA e dados.", "Connects industrial experience with AI and data solution building."),
        tr(lang, "Reúne profundidade quantitativa, engenharia de processos e execução em software.", "Brings together quantitative depth, process engineering, and software execution."),
        tr(lang, "Transita entre contexto executivo, técnico e didático com comunicação clara.", "Works across executive, technical, and teaching contexts with clear communication."),
        tr(lang, "Sustenta um perfil consistente para inovação aplicada, produtos técnicos e transformação digital.", "Sustains a strong profile for applied innovation, technical products, and digital transformation."),
    ]
    ui = {
        "title": tr(lang, "Currículo", "Resume"),
        "subtitle": tr(lang, "Acesse experiência, formação, áreas de foco e stack técnica em uma leitura organizada.", "Access experience, education, focus areas, and technical stack in an organized view."),
        "profile_chip": tr(lang, "Perfil profissional", "Professional profile"),
        "profile_title": tr(lang, "Veja um perfil híbrido entre indústria, dados, software e ensino", "Review a hybrid profile across industry, data, software, and teaching"),
        "experience_sub": tr(lang, "Leia as experiências por eixo de contribuição.", "Read the experience grouped by contribution track."),
        "education_title": tr(lang, "Formação acadêmica", "Academic background"),
        "education_sub": tr(lang, "Veja a base que conecta automação, engenharia, otimização e sistemas.", "Review the background connecting automation, engineering, optimization, and systems."),
        "subjects_title": tr(lang, "Disciplinas e atuação acadêmica", "Subjects and academic work"),
        "subjects_sub": tr(lang, "Acesse as áreas de ensino com componente aplicado.", "Access the teaching areas with applied focus."),
        "focus_title": tr(lang, "Áreas de foco", "Focus areas"),
        "focus_sub": tr(lang, "Veja onde a atuação técnica se concentra.", "See where the technical work is concentrated."),
        "stack_title": tr(lang, "Stack e especialidades", "Stack and specialties"),
        "stack_sub": tr(lang, "Acesse tecnologias, métodos e contextos que estruturam a experiência profissional.", "Access the technologies, methods, and contexts that structure the professional experience."),
        "diff_title": tr(lang, "Diferenciais", "Differentiators"),
        "download_label": tr(lang, "Baixar CV em PDF", "Download CV as PDF"),
        "contact_label": tr(lang, "Abrir contato", "Open contact"),
    }
    return render_template('resume.html', lang=lang, current_lang=lang, professional_summary=professional_summary, resume_stats=resume_stats, experience_groups=experience_groups, education=education, teaching_disciplines=teaching_disciplines, focus_areas=focus_areas, stack_groups=stack_groups, achievements=achievements, ui=ui)


@main_bp.route('/resume/download')
def download_resume():
    docs_dir = current_app.root_path + '/static/docs'
    return send_from_directory(docs_dir, 'pedro_candido_profile.pdf', as_attachment=True)


@main_bp.route('/lab')
def lab():
    lang = get_lang()
    demos = [
        {
            "title": tr(lang, "Clusterização interativa", "Interactive clustering"),
            "description": tr(lang, "Veja demos para segmentação, leitura executiva e análise comparativa de grupos.", "Review demos for segmentation, executive reading, and comparative group analysis."),
            "tags": ["K-Means", "DBSCAN", tr(lang, "Interpretação", "Interpretation")],
        },
        {
            "title": tr(lang, "Aplicações em Flask e Streamlit", "Flask and Streamlit applications"),
            "description": tr(lang, "Acesse protótipos voltados para ensino, analytics e aplicações orientadas a interface.", "Access prototypes built for teaching, analytics, and interface-driven applications."),
            "tags": ["Flask", "Streamlit", "UX"],
        },
        {
            "title": tr(lang, "ESP32 e tempo real", "ESP32 and real-time systems"),
            "description": tr(lang, "Consulte ideias e experimentos com embarcados, sensores, tarefas e RTOS.", "Review ideas and experiments with embedded systems, sensors, tasks, and RTOS."),
            "tags": ["ESP32", "RTOS", "IoT"],
        },
        {
            "title": tr(lang, "Analytics e otimização", "Analytics and optimization"),
            "description": tr(lang, "Abra frentes voltadas a planejamento, estatística, modelos e apoio à decisão.", "Open tracks focused on planning, statistics, models, and decision support."),
            "tags": [tr(lang, "Estatística", "Statistics"), tr(lang, "Otimização", "Optimization"), "Analytics"],
        },
    ]
    ui = {
        "title": "Lab",
        "subtitle": tr(lang, "Acesse demos, protótipos e aplicações demonstrativas com foco técnico e didático.", "Access demos, prototypes, and demonstrative applications with technical and teaching focus."),
    }
    return render_template('lab.html', demos=demos, lang=lang, ui=ui)


@main_bp.route('/contact')
def contact():
    lang = get_lang()
    ui = {
        "title": tr(lang, "Contato", "Contact"),
        "subtitle": tr(lang, "Use esta página para contato profissional, consultoria, docência, parcerias e projetos em tecnologia aplicada.", "Use this page for professional contact, consulting, teaching, partnerships, and projects in applied technology."),
        "card_title": tr(lang, "Canais de contato", "Contact channels"),
        "card_text": tr(lang, "Escolha o canal mais adequado para currículo, projetos, consultoria, oportunidades e colaboração técnica.", "Choose the most suitable channel for resume requests, projects, consulting, opportunities, and technical collaboration."),
        "github_label": tr(lang, "Abrir GitHub", "Open GitHub"),
        "linkedin_label": tr(lang, "Abrir LinkedIn", "Open LinkedIn"),
        "resume_label": tr(lang, "Baixar CV", "Download CV"),
    }
    contact_info = {
        "email": "pedrocnf@gmail.com",
        "domain": current_app.config.get("SITE_DOMAIN", "tekforge.com.br"),
        "github": f"https://github.com/{current_app.config.get('GITHUB_USERNAME', 'pedrocnf')}",
        "linkedin": "https://www.linkedin.com/in/pedrocnf/",
    }
    return render_template('contact.html', lang=lang, ui=ui, contact_info=contact_info)
