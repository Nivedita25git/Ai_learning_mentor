from utils.memory_store import load_memory, save_memory

memory = load_memory()


def set_memory(key, value):
    memory[key] = value
    save_memory(memory)


def get_memory(key):
    return memory.get(key)


def add_chat(role, message):
    memory.setdefault("chat_history", [])
    memory["chat_history"].append({"role": role, "message": message})
    save_memory(memory)