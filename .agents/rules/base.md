<!-- AI Harness Rule: This is a contextually loaded rule file for the LLM. Do NOT modify this file unless explicitly requested by the user. -->
---
trigger: always_on
---

# Antigravity Agent Rules

1. **Language**: Always respond in Korean (한국어). Even if the user asks in English or the context is technical, provide explanations in Korean unless explicitly requested otherwise.
2. **Tasks & Plans**: Always write the 'Implementation Plan' and 'Walkthrough' steps in Korean.
3. **Code Comments**: Always write code comments in Korean.
4. **Project Governance**: You MUST strictly adhere to the repository navigation and behavioral boundaries defined in `.agents/AGENTS.md`. Always check `.agents/AGENTS.md` first to understand the layout, quality standards, and architectural constraints of the project before making structural changes.
