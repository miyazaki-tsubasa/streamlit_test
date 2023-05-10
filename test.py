

import streamlit as st

#st.title('streamlit Tutorial')
#st.header('This is a header')
#st.subheader('This is a subheader')
#st.text('Hello World!,this is text')

# st.write()はMarkdown表記対応
#st.write('# headline1')
# 以下のように明示的に書くことも可能
#st.markdown('## headline2')

st.write('# 全体の流れ')
st.text('deep learningに関して、実装結果を踏まえてアルゴリズムなどをまとめる。')
st.text('手法による精度の違いなど')



#エラーメッセージ表示
if len(usecols) == 0 or len(names) == 0:
    st.error('解析対象の列が指定されていません。')
