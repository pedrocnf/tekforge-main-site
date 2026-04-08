from flask import Blueprint, render_template, request, abort

teaching_bp = Blueprint("teaching", __name__)


def get_lang():
    lang = request.args.get("lang", "pt")
    return lang if lang in {"pt", "en"} else "pt"


def tr(lang, pt, en):
    return pt if lang == "pt" else en


def build_courses(lang):
    return {
        "disciplina-1": {
            "badge": tr(lang, "Disciplina 1", "Course 1"),
            "title": tr(lang, "Inteligência Artificial", "Artificial Intelligence"),
            "subtitle": tr(lang, "Modelagem, avaliação de modelos e aplicações orientadas a problema", "Modeling, model evaluation, and problem-driven applications"),
            "workload": tr(lang, "80 horas · Graduação", "80 hours · Undergraduate"),
            "materials": tr(lang, "Slides, notebooks, estudos de caso, exercícios e mini-projetos", "Slides, notebooks, case studies, exercises, and mini-projects"),
            "description": tr(lang, "Disciplina voltada para fundamentos e aplicações contemporâneas de IA, com foco em modelagem, métricas, leitura crítica de resultados e construção de repertório técnico para projetos práticos.", "Course focused on AI foundations and contemporary applications, with emphasis on modeling, metrics, critical reading of results, and technical repertoire for practical projects."),
            "topics": [tr(lang, "Supervisionado e não supervisionado", "Supervised and unsupervised learning"), tr(lang, "Métricas e validação", "Metrics and validation"), tr(lang, "Interpretação de modelos", "Model interpretation"), tr(lang, "Casos de uso em negócio", "Business use cases")],
        },
        "disciplina-2": {
            "badge": tr(lang, "Disciplina 2", "Course 2"),
            "title": tr(lang, "Programação em Tempo Real", "Real-Time Programming"),
            "subtitle": tr(lang, "ESP32, RTOS, tarefas concorrentes e práticas embarcadas", "ESP32, RTOS, concurrent tasks, and embedded practice"),
            "workload": tr(lang, "80 horas · Graduação", "80 hours · Undergraduate"),
            "materials": tr(lang, "Práticas, simulações, códigos, desafios e relatórios", "Practices, simulations, code, challenges, and reports"),
            "description": tr(lang, "Disciplina organizada para introduzir tempo real, concorrência, temporização, leitura de periféricos e uso de RTOS em contexto didático com laboratório.", "Course designed to introduce real-time concepts, concurrency, timing, peripheral handling, and RTOS use in a teaching lab context."),
            "topics": [tr(lang, "Tarefas, filas e temporização", "Tasks, queues, and timing"), tr(lang, "ESP32 e periféricos", "ESP32 and peripherals"), tr(lang, "Sincronização e eventos", "Synchronization and events"), tr(lang, "Boas práticas em laboratório", "Good lab practices")],
        },
        "disciplina-3": {
            "badge": tr(lang, "Disciplina 3", "Course 3"),
            "title": tr(lang, "Introdução à IA", "Introduction to AI"),
            "subtitle": tr(lang, "Fundamentos, história, ética e leitura crítica da área", "Foundations, history, ethics, and critical reading of the field"),
            "workload": tr(lang, "40 horas · Graduação", "40 hours · Undergraduate"),
            "materials": tr(lang, "Textos, mapas conceituais, slides e estudos introdutórios", "Texts, concept maps, slides, and introductory studies"),
            "description": tr(lang, "Disciplina introdutória desenhada para construir repertório conceitual sólido antes do aprofundamento em machine learning e aplicações. Integra fundamentos, história, ética e leitura crítica.", "Introductory course designed to build a solid conceptual repertoire before deeper work in machine learning and applications. It integrates foundations, history, ethics, and critical reading."),
            "topics": [tr(lang, "História da IA e seus ciclos", "History of AI and its cycles"), tr(lang, "Agentes, busca e representação", "Agents, search, and representation"), tr(lang, "IA simbólica e aprendizado de máquina", "Symbolic AI and machine learning"), tr(lang, "Impacto social e profissional da IA", "Social and professional impact of AI")],
        },
    }


@teaching_bp.route("/")
def teaching_home():
    lang = get_lang()
    disciplines = []
    for slug, course in build_courses(lang).items():
        disciplines.append({"slug": slug, **course})
    ui = {
        "title": tr(lang, "Sala de Aula", "Classroom"),
        "subtitle": tr(lang, "Acesse disciplinas em formato de cards, com conteúdo demonstrativo e navegação direta.", "Access courses in card format, with demonstrative content and direct navigation."),
    }
    return render_template("teaching.html", disciplines=disciplines, lang=lang, current_lang=lang, ui=ui)


@teaching_bp.route('/<slug>')
def discipline_page(slug):
    lang = get_lang()
    courses = build_courses(lang)
    course = courses.get(slug)
    if not course:
        abort(404)
    return render_template('classroom/discipline.html', course=course, lang=lang, current_lang=lang)
