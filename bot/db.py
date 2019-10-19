import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE music(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        file_id TEXT NOT NULL,
        right_answer TEXT NOT NULL,
       wrong_answer TEXT NOT NULL
);""")

cur.execute("""INSERT INTO music(id, file_id, right_answer, wrong_answer) VALUES(1, "AwADAgAD0wQAApksWEnLrhR2vZGPVBYE",
        "Rihanna-Diamond", "Rihanna-What's My Name,Rihanna-Umbrella,Shakira-Blame,Birdy-Wings"),
        (2, "AwADAgAD9gUAAiEWWEmof4jfR5QoARYE", "Shakira-Hips Don't Lie", "Rihanna-Cry,Shakira-La La La,Birdy-Skinny Love"),
        (3, "AwADAgADGQYAAnEwWEkO7T1XsMdvcBYE", "Nemra-Born in 94", "Scorpions-White Dove,System Of A Down-Toxicity,Scorpions-Wind Of Chang"),
        (4, "AwADAgAD-AUAAiEWWEmnDINxWgqC7BYE", "Mani Beats-N&N", "Grace - You Don't Own Me,Shakira-Loca,Rihanna-Work");""")
        

conn.commit()
conn.close()
