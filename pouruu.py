import streamlit as st
import hashlib

st.set_page_config(page_title="For You ❤️", page_icon="💖")

name = "Pouruuuu"  # change

photo1 = r"C:\Users\Shweta\Downloads\Snapchat-1679850145.jpg"
photo2 = r"C:\Users\Shweta\Downloads\IMG20260204170954.jpg"
photo3 = r"C:\Users\Shweta\Downloads\IMG-20260114-WA0123.jpeg"
photo4 = r"C:\Users\Shweta\Downloads\IMG20250925135108.jpg"
photo5 = r"C:\Users\Shweta\Downloads\IMG-20260223-WA0054.jpg"


music_file = r"C:\Users\Shweta\Downloads\Standard recording 3.mp3"

stored_hash = "202178ea4189d11c52dd1082d6f8a52032e7eea51122d7f8f1e46d8fdc54e744"

def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

st.title(f"For {name} 💕")

st.write(f"""
Hey {name}...

meeting u totally Gods plan haa khara baba pun lucky u and me too v met each other. bus stop pe rukke bus ka wait karne 
journey and us gossiping there too abt whoever v saw there. halu jaa bolyavr tu haa me chalavte bolnari shaani pun all was worth it. definetely v r opposite in may things pun tri teh ek mekana affect nhi houn 
sambhalun ghena was so imp. teh fights,misunderstanding  tr definetely disturbing asayche pun wht i all realized tyani is v both affect each other kiti hee bhandlo tri garaj aahe ani farak pun padto.
teh double meaning jokes bhendi aaple ani from unknowns to common friends to classmate to bestest friend to now also my project member was all more than worth it.ani hee majhi maitrii fakt 4yrs chi ajibaat ch nahi bilkul pun lifetime & forever chi aahe me nasel call karen kadhi tu bindaas call kr pun tujhi pratyek new ghosht abt u tyacha nantr mala mahiti asli pahije jashi aata mahiti aste,samajla my pouruuuu?
""")

st.header("You matter to me ❤️")

st.write("""
- You make everything lighter  
- you are imp baby  
- You make me feel understood  

That’s not something I take for granted.
""")

st.image(photo1, caption="You & me 💖")
st.image(photo2, caption="Best chaos ever 😂")
st.image(photo3, caption="masti rukni nhi chaiye 💖")
st.image(photo4, caption="our bond 💖")
st.image(photo5, caption="💖")

audio = open(music_file, "rb").read()
st.audio(audio)

st.subheader("My girliee boyfriend 😅")
st.write("""
You understand me without explanation  
- mla justification chi garaj nhi lagtat when wid u 
- You stay when things get messy  

That’s rare. And I value it.
""")

if st.button("Click if you love me "):
    st.success("Thank you 😭❤️")

# SECRET
st.markdown("---")
secret = st.text_input("Secret code 🤫", type="password")

if secret:
    if hash_text(secret) == stored_hash:
        st.balloons()
        st.success("Unlocked ❤️")

        st.write(f"""
        {name},

        You are my comfort person.

        Even when I don’t say things,
        you get it.

        I don’t want to lose that.
        Ever.

        Stay with me ❤️
        """)
    else:
        st.error("Wrong code 😤")