# SEO Article Auto Writer

## Overview
SEO Article Auto Writer is an **AI automation tool** that generates SEO-optimized articles **based on real-time keyword trends and business analysis**. The project uses **CrewAI** agents to analyze a website, determine the best content strategy, find trending topics, and generate a high-quality SEO article.

---

## How It Works
The **SEO Article Auto Writer** follows a **step-by-step AI-driven process** to create an article tailored to the website’s niche and trending topics.

### **1. Website Analysis**
- Scrapes and analyzes a given website.
- Identifies its niche, services, and potential content topics.

### **2. Content Strategy Generation**
- Determines the most valuable article type (e.g., listicle, how-to guide, case study) for SEO.

### **3. Keyword & Trend Research**
- Uses **Google Trends** to find trending topics and high-ranking keywords.
- Analyzes search intent, ranking difficulty, and keyword competitiveness.

### **4. Article Writing**
- Generates a **1500-2000 word** SEO-optimized article with proper structure, keyword integration, and readability.

---

## Installation & Setup
### **1. Clone the repository**
```bash
git clone https://github.com/paquino11/seo_art_auto_crewai.git
cd seo_art_auto_crewai
```

### **2. Create a virtual environment and activate it**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### **3. Install dependencies**
```bash
crewai install
```

### **4. Add Google Trends API**
```bash
uv add google-trends-api
```

### **5. Create a `.env` file and set up API keys**
```bash
export MODEL=gpt-4o-mini
export OPENAI_API_KEY=your_openai_api_key
export SERPER_API_KEY=your_serper_api_key
export SERPAPI_API_KEY=your_serpapi_api_key
```

### **6. Select website in `main.py`**
Edit `main.py` to define the website to analyze:
```python
def run():
    """
    Run the crew.
    """
    inputs = {
        'website': 'your_website_url',
        'current_year': str(datetime.now().year)
    }
```

### **7. Run the tool**
```bash
crewai run
```

---

## CrewAI Agents
The system uses **CrewAI** agents with distinct roles:

| **Agent**              | **Role**                                              |
|------------------------|------------------------------------------------------|
| **Website Analyzer**   | Scrapes website & extracts key business information |
| **Content Strategist** | Determines the best article type for SEO based on the website's info            |
| **SEO Trend Researcher** | Finds trending keywords & Google search trends  |
| **SEO Writer**         | Generates a high-quality, optimized article         |

---

## Example Output
An **SEO article** is generated in the `/output/article.md` file, structured as follows:

```markdown
# The Future of Real Estate Marketing: Top 5 Trends in 2024

## Introduction
In today’s digital age, real estate marketing is evolving rapidly. With the rise of AI and automation, businesses must stay ahead of the curve...

## 1. AI-Powered Property Listings
- AI-driven tools now help buyers find the perfect home.
- Personalization improves customer engagement.

## 2. Virtual Tours & Augmented Reality
- Real estate firms are integrating VR technology for property viewings.

...

## Conclusion
To stay competitive in 2024, real estate businesses must adapt to digital innovations and AI-powered strategies.
```

---

## Contributing
- Feel free to fork the repo and submit **pull requests**.
- Report any **issues or suggestions** in the Issues tab.


