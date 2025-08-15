# LangChain Chains

This repository demonstrates **four different chain types** available in [LangChain](https://www.langchain.com/), showing how they can be used to build powerful, composable AI workflows.

## 📂 Chain Types Included
1. **Simple Chain**
2. **Sequential Chain**
3. **Parallel Chain**
4. **Conditional Chain**

---

## 1. Simple Chain
A **Simple Chain** passes input through a single sequence of operations.

**Advantages**
- Easy to implement
- Minimal configuration
- Ideal for small, focused tasks

**Use Case**
- Taking a question and returning a concise answer
- Summarizing a short text snippet

---

## 2. Sequential Chain
A **Sequential Chain** runs multiple chains **one after another**, passing the output of one chain as the input to the next.

**Advantages**
- Clear control over execution order
- Good for multi-step reasoning
- Easy to debug

**Use Case**
- First summarizing a document, then translating it
- Generating an outline, then expanding it into a full draft

---

## 3. Parallel Chain
A **Parallel Chain** runs multiple chains **at the same time** using the same input, then aggregates their outputs.

**Advantages**
- Faster execution for independent tasks
- Can handle multiple perspectives or processing methods in parallel

**Use Case**
- Getting answers from multiple LLM prompts for comparison
- Running classification and sentiment analysis simultaneously

---

## 4. Conditional Chain
A **Conditional Chain** decides which chain to run **based on input conditions**.

**Advantages**
- Flexible, dynamic behavior
- Saves computation by avoiding unnecessary steps

**Use Case**
- Routing a user query to either a summarizer or a translator based on query type
- Detecting language and choosing the appropriate processing chain
