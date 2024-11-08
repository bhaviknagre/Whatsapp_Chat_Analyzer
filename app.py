import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Chosse a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    st.dataframe(df)

    user_list = df['user'].unique().tolist()
    user_list.remove('group notification')
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user = st.sidebar.selectbox("Show analysis wrt",user_list)

    if st.sidebar.button("Show analysis"):


        num_messages,words,num_media_messages,num_links = helper.fetch_stats(selected_user,df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)


        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Total Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.title(num_links)

        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'],color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x,df = helper.most_busy_users(df)
            fig, ax =plt.subplots()
            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values,color='fuchsia')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(df)
