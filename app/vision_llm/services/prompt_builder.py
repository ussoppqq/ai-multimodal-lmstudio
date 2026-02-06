def build_vision_prompt(objects: list) -> str:
    if not objects:
        return (
            "Tidak ada objek yang terdeteksi pada gambar. "
            "Jelaskan bahwa tidak ada informasi visual yang tersedia."
        )

    object_list = "\n".join(
        f"- {obj['label']} (confidence {obj['confidence']:.2f})"
        for obj in objects
    )

    prompt = f"""
Kamu adalah asisten AI.

Kamu diberikan hasil dari sistem object detection.
Gunakan HANYA objek yang terdeteksi di bawah ini untuk membuat penjelasan.

Objek yang terdeteksi:
{object_list}

Tolong jelaskan dalam Bahasa Indonesia:
1. Apa yang kemungkinan terjadi pada gambar
2. Jenis lingkungan atau situasi pada gambar
3. Observasi yang relevan berdasarkan objek yang terdeteksi

Jika informasi tidak tersedia dari objek, jangan membuat asumsi tambahan.
Jawab dengan bahasa yang jelas dan natural.
"""
    return prompt.strip()
