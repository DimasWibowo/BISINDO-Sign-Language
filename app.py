import streamlit as st
from pytube import YouTube
import hydralit_components as hc
from streamlit.components.v1 import html

def nav_page(page_name, timeout_secs=10):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)

st.set_page_config(
    page_title='bisindo',
    layout='wide',
    initial_sidebar_state='expanded',
)


# Fungsi untuk mendapatkan judul dari YouTube URL tanpa imbuhan "Bisindo"
def get_video_title(youtube_url):
    try:
        yt = YouTube(youtube_url)
        title = yt.title
        # Menghapus "Bisindo" dari judul dan mengambil kata setelahnya
        if "Bisindo" in title:
            title_parts = title.split("Bisindo")
            if len(title_parts) > 1:
                return title_parts[1].strip()
        return title
    except Exception as e:
        st.error(f"Gagal mendapatkan judul dari URL {youtube_url}.")
        st.error(str(e))
        return "Video Tidak Tersedia"

# Fungsi untuk menampilkan video dari YouTube
def display_youtube_video(youtube_url):
    video_id = youtube_url.split("=")[-1] if "=" in youtube_url else youtube_url.split("/")[-1].split("?")[0]
    video_url = f"https://www.youtube.com/embed/{video_id}"
    st.write(f'<iframe width="280" height="157" src="{video_url}" frameborder="0" allowfullscreen style="margin-bottom: 20px;"></iframe>', unsafe_allow_html=True)

def main():
    # Menyesuaikan margin dan lebar kolom agar tidak menumpuk
    over_theme = {'txc_inactive': 'white','menu_background':'green','txc_active':'green','option_active':'white'}
    font_fmt = {'font-class':'h2','font-size':'150%', 'width':'200px'}


    menu = hc.nav_bar(
        menu_definition=[
            {"label": "Beranda"},
            {"label": "Belajar"},
            {"label": "Mini Games"},           
            {"label": "Tentang"}
        ],
        key='PrimaryOption',
        override_theme=over_theme,
        # font_styling=font_fmt,
        # horizontal_orientation=True,
    )


    st.markdown(
        """
        <style>
            .st-df {
                column-gap: 20px;
                padding: 0px !important;
            }
            .st-cg {
                padding: 0px !important;
                margin: 0px !important;
            }
            header {
                text-align: center;
            }
            .stApp {
                text-align: center;
            }
            .st-emotion-cache-z5fcl4 {
            padding:0!important;
            }

        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Tampilan untuk "Beranda"
    if menu == "Belajar":
        st.title("Pelajari Bahasa Isyarat Indonesia")

        youtube_urls = [
            "https://www.youtube.com/watch?v=GCFfwXFi6hA",
            "https://www.youtube.com/watch?v=S-2Lj8OzPqQ",
            "https://www.youtube.com/watch?v=MvyeZK6hHPg",
            "https://www.youtube.com/watch?v=w2w1RwtyGnI",
            "https://www.youtube.com/watch?v=1zexupTxhjY",
            "https://www.youtube.com/watch?v=yF5D1P61ruc",
            "https://www.youtube.com/watch?v=RSLinLUs0no",
            "https://www.youtube.com/watch?v=dIM8D0UzTcM",
            "https://www.youtube.com/watch?v=0kym9mtmJHY",
            "https://www.youtube.com/watch?v=yiNQZ4qP-gQ",
            "https://www.youtube.com/watch?v=oFnNk1hXvJQ",
            "https://www.youtube.com/watch?v=AEpD4bCMFF8",
            "https://www.youtube.com/watch?v=-xeL9SVqouw",
            "https://www.youtube.com/watch?v=CMFnFbqVVsM",
            "https://www.youtube.com/watch?v=A6VuG_vz5KI",
            "https://www.youtube.com/watch?v=KmGQxAMJJ5M",
            "https://www.youtube.com/watch?v=pnZFh69CM38",
            "https://www.youtube.com/watch?v=MePOVCZDgLk",
            "https://www.youtube.com/watch?v=sQOpGjJTdpo",
            "https://www.youtube.com/watch?v=qzRnU5vuCSo",
            "https://www.youtube.com/watch?v=im2wtb77WnQ",
            "https://www.youtube.com/watch?v=q0zJl-IhTcc",
            "https://www.youtube.com/watch?v=sGjptC-vJ30",
            "https://www.youtube.com/watch?v=1OF6gpG3fFs",
            "https://www.youtube.com/watch?v=3deDWmIofrk",
            "https://www.youtube.com/watch?v=Xc4qx-mOLPY",
            "https://www.youtube.com/watch?v=l94RDnOfmeg",
            "https://www.youtube.com/watch?v=pndvoL6wNck",
            "https://www.youtube.com/watch?v=xZOOLmwVOMI",
            "https://www.youtube.com/watch?v=d96g8WoWlKQ",
            "https://www.youtube.com/watch?v=5hYs_KLpkHg",
            "https://www.youtube.com/watch?v=IamAOXWNltM",
            "https://www.youtube.com/watch?v=vXJ8ZgnHqfk",
            "https://www.youtube.com/watch?v=HjJkym6puho",
            "https://www.youtube.com/watch?v=Mjn58G6caoE",
            "https://www.youtube.com/watch?v=x52qePxNJ3c",
            "https://www.youtube.com/watch?v=CpbMam8sW6o",
            "https://www.youtube.com/watch?v=ZjtxSsfPSCk",
            "https://www.youtube.com/watch?v=d1ZlBAPnvxA",
            "https://www.youtube.com/watch?v=fh7qEh0o3Og",
            "https://www.youtube.com/watch?v=1ikWnb32OYk",
            "https://www.youtube.com/watch?v=ehzPuduoGDA",
            "https://www.youtube.com/watch?v=lBhIR2ZbZ7k",
            "https://www.youtube.com/watch?v=5cSgPUwH244",
            "https://www.youtube.com/watch?v=rOuKqjW5CpE",
            "https://www.youtube.com/watch?v=Kpzc5WCSXVU",
            "https://www.youtube.com/watch?v=9rlOk6HjQMM",
            "https://www.youtube.com/watch?v=rrJo-FV6yf0",
            "https://www.youtube.com/watch?v=sra7h0dqzy0",
            "https://www.youtube.com/watch?v=BqzqzU3Vsb4",
            "https://www.youtube.com/watch?v=5-aZ3vMVa9g",
            "https://www.youtube.com/watch?v=bugvwCHPzpw"
        ]

        col1, col2, col3, col4 = st.columns(4)

        for i, url in enumerate(youtube_urls):
            try:
                video_title = get_video_title(url)
                if i % 4 == 0:
                    with col1:
                        st.markdown(
                            f"<h3 style='text-align: center;'>{video_title}</h3>",
                            unsafe_allow_html=True
                        )
                        display_youtube_video(url)
                elif i % 4 == 1:
                    with col2:
                        st.markdown(
                            f"<h3 style='text-align: center;'>{video_title}</h3>",
                            unsafe_allow_html=True
                        )
                        display_youtube_video(url)
                elif i % 4 == 2:
                    with col3:
                        st.markdown(
                            f"<h3 style='text-align: center;'>{video_title}</h3>",
                            unsafe_allow_html=True
                        )
                        display_youtube_video(url)
                else:
                    with col4:
                        st.markdown(
                            f"<h3 style='text-align: center;'>{video_title}</h3>",
                            unsafe_allow_html=True
                        )
                        display_youtube_video(url)
            except Exception as e:
                st.error(f"Terjadi kesalahan dalam memuat video dari URL {url}.")
                st.error(str(e))

    # elif menu == "Mini Games":
    #     mini_game()

    elif menu == "Mini Games":
        nav_page("game")

if __name__ == "__main__":
    main()
