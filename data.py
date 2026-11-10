SITE_URL = "https://karthiksai08.github.io"  # after deploying, put your site URL here, e.g. "https://karthiksai08.github.io/portfolio" (used for link previews)

WHY = [
    ("Production-minded", "My ATMS traffic-violation detector is built for live RTSP highway cameras, and every model I build is served as a FastAPI service rather than left in a notebook."),
    ("Evaluation-first", "Leakage-safe splits, per-class metrics and benchmarks: 85% on a 40-case Text-to-SQL suite (plus 265 manual questions), and NDCG@3 raised from 0.758 to 0.836."),
    ("Model to API to database", "I work across the stack: fine-tuning and retrieval on one side, REST and gRPC services, SQL Server and PostgreSQL on the other."),
]

PROFILE = {
    "name": "Karthik Sai S",
    "role": "AI/ML Engineer",
    "tagline": "I build GenAI, RAG and computer vision systems and ship them as FastAPI services.",
    "location": "Chennai, India",
    "open_to": "Chennai, Bengaluru, Hyderabad, Kochi, Coimbatore",
    "email": "karthiksai.0812@gmail.com",
    "github": "https://github.com/KarthikSai08",
    "linkedin": "https://linkedin.com/in/karthiksai0812",
    "resume": "/static/Karthik_Sai_S_Resume.pdf",
    "summary": [
        "I'm an AI/ML engineer with 6+ months of internship experience building Generative AI, RAG, NLP and computer vision systems, plus 3 months of ASP.NET Core backend work on a production SQL Server application.",
        "I care about systems that hold up outside a notebook: leakage-safe evaluation, guardrails, validation layers and confidence routing, all exposed through clean APIs.",
    ],
}

STATS = [
    ("6+ months", "AI/ML internship"),
    ("~96%", "Email classifier accuracy"),
    ("85%", "Text-to-SQL benchmark pass rate"),
    ("15,000+", "Images in the ATMS dataset"),
]

PROJECTS = [
    {
        "title": "ATMS: AI traffic violation detection",
        "slug": "atms",
        "tag": "Live production",
        "featured": True,
        "points": [
            "Fine-tuning YOLO11 on 15,000+ annotated images to detect helmet, no-helmet, triple riding, seatbelt and vehicle classes from live RTSP highway cameras.",
            "Two-stage pipeline (vehicle detection, then cropped violation detection) with a head-count rule for triple riding, plus oversampling and targeted augmentation for class imbalance.",
            "Time-block data splits prevent leakage; evaluated per class against precision/recall targets aligned to NHAI benchmarks.",
        ],
        "stack": ["Python", "YOLO11", "PyTorch", "OpenCV", "RTSP", "FastAPI"],
        "link": None,
        "demo": None,    # live demo URL, e.g. "https://..."
        "images": [],    # e.g. ["1.png", "2.png"] inside static/projects/<slug>/
    },
    {
        "title": "Enterprise Text-to-SQL assistant",
        "slug": "text-to-sql",
        "tag": "85% pass rate",
        "featured": True,
        "points": [
            "Two-stage hybrid retrieval (BM25 + BGE-M3 + Reciprocal Rank Fusion) with cross-encoder reranking picks the right 2-5 tables from a 68-table, 717-column schema.",
            "Three-layer hallucination defense: retrieval-constrained context, sqlglot AST validation and corrective retries, plus 30 PII guardrail patterns.",
            "Validated on a 40-case benchmark and 265 manual questions.",
        ],
        "stack": ["FastAPI", "Groq LLaMA 3.1", "BGE-M3", "ChromaDB", "sqlglot", "SQL Server"],
        "link": "https://github.com/KarthikSai08/enterprise-ai-assistant",
        "demo": None,    # live demo URL, e.g. "https://..."
        "images": [],    # e.g. ["1.png", "2.png"] inside static/projects/<slug>/
    },
    {
        "title": "Email classification and real-time routing",
        "slug": "email-routing",
        "tag": "~96% accuracy",
        "featured": False,
        "points": [
            "Fine-tuned DeBERTa-v3-base for 10-class department classification; mail below 0.70 confidence goes to a default address.",
            "Event-driven pipeline (Gmail API watch, Pub/Sub push) persists message and history IDs for exactly-once processing across restarts.",
        ],
        "stack": ["DeBERTa-v3", "PyTorch", "FastAPI", "Gmail API", "OAuth 2.0", "Pub/Sub"],
        "link": "https://github.com/KarthikSai08/ai-email-automation",
        "demo": None,    # live demo URL, e.g. "https://..."
        "images": [],    # e.g. ["1.png", "2.png"] inside static/projects/<slug>/
    },
    {
        "title": "Supplier ranking advisor",
        "slug": "supplier-ranking",
        "tag": "NDCG@3 0.758 to 0.836",
        "featured": False,
        "points": [
            "Leakage-safe LambdaMART ranker, with price (R2 0.84) and return-risk (AUC 0.76) sub-models.",
            "TreeSHAP explanations show why each supplier is ranked where it is.",
        ],
        "stack": ["LambdaMART", "XGBoost", "SHAP", "scikit-learn", "pandas"],
        "link": None,
        "demo": None,    # live demo URL, e.g. "https://..."
        "images": [],    # e.g. ["1.png", "2.png"] inside static/projects/<slug>/
    },
    {
        "title": "Read-only AI support chatbot",
        "slug": "support-chatbot",
        "tag": "Guarded SQL",
        "featured": False,
        "points": [
            "Generates fix SQL and step-by-step instructions for support-team data issues without ever writing to the database.",
            "A sqlglot Query Guard checks every statement; PaddleOCR reads screenshots.",
        ],
        "stack": ["Groq LLM", "sqlglot", "PaddleOCR", "FastAPI"],
        "link": None,
        "demo": None,    # live demo URL, e.g. "https://..."
        "images": [],    # e.g. ["1.png", "2.png"] inside static/projects/<slug>/
    },
]

SKILLS = [
    ("Generative AI and LLMs", ["LLMs", "RAG", "Prompt engineering", "LoRA / QLoRA", "PEFT", "Embeddings", "ChromaDB", "Hybrid search", "Reranking", "LLM evaluation", "Guardrails"]),
    ("LLM frameworks and observability", ["LangChain", "LangGraph", "LangSmith", "MCP", "Hugging Face Transformers"]),
    ("Agentic AI", ["Multi-agent systems", "Tool calling", "Human-in-the-loop workflows", "Agent evaluation and tracing"]),
    ("Machine learning", ["scikit-learn", "XGBoost", "PyTorch", "Hugging Face", "NLP", "Feature engineering", "Learning-to-rank", "SHAP", "Class imbalance", "Leakage prevention"]),
    ("Computer vision", ["YOLO11", "Object detection", "OpenCV", "PaddleOCR", "Data augmentation"]),
    ("Backend and data", ["Python", "FastAPI", "REST", "gRPC", "ASP.NET Core", "Dapper", "JWT", "OAuth 2.0", "SQL Server", "PostgreSQL", "SQL", "pandas", "NumPy"]),
    ("Cloud and tools", ["Git", "GitHub", "Google Cloud", "Pub/Sub", "Gmail API"]),
]

EXPERIENCE = [
    {
        "title": "AI/ML Engineer Intern",
        "org": "WeServeCodes, Ahmedabad",
        "period": "Apr 2026 - Present",
        "points": [
            "Built Text-to-SQL, email-routing and ATMS traffic-violation systems as FastAPI services with confidence routing, AST-based SQL validation and PII guardrails.",
            "Built a leakage-safe supplier ranking advisor that raised NDCG@3 from 0.758 to 0.836.",
        ],
    },
    {
        "title": ".NET Backend Developer Intern",
        "org": "WeServeCodes, Ahmedabad",
        "period": "Jan 2026 - Mar 2026",
        "points": [
            "Developed REST and gRPC services in ASP.NET Core (Clean Architecture, CQRS with MediatR) for a production SQL Server application.",
            "Migrated ADO.NET to Dapper, fixed N+1 queries, and added JWT authentication, rate limiting and idempotency safeguards.",
        ],
    },
]

EDUCATION = [
    ("M.Sc. Computer Science", "Hindustan College of Arts and Science", "2025", "CGPA 8.0/10"),
    ("B.Sc. Computer Science", "Dhanraj Baid Jain College of Arts and Science", "2023", "CGPA 7.9/10"),
]

PUBLICATION = {
    "title": "A Review on Supervised Machine Learning Algorithms",
    "venue": "ICFTAI'24, International Conference on Future Trends in AI",
    "date": "Oct 2024",
}
