import streamlit as st
import pandas as  pd
import os
from streamlit_option_menu import option_menu
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from pandas_profiling import profile_report,ProfileReport
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from autoviz.AutoViz_Class import AutoViz_Class 

st.set_page_config(page_title="AI WITH DATA", page_icon="📊", layout="centered", initial_sidebar_state="auto", menu_items=None)




hide_st_style  = """
    <style>

    footer {visibility:hidden;}
  
    </style>
    """
st.markdown(hide_st_style,unsafe_allow_html = True)


st.header("Business Intelligence Web ")


updated = 0




 
selected = option_menu(
        menu_title = "Navbar",
        options = ["Data set","Cleaning","EDA","Machine Learning","Dashboard","Deployment"],
        menu_icon = "cast",
        default_index = 0,
        orientation = "horizontal",
        styles = {
        
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "15px", "font-style":"Time new roman","text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "pink"},
        }
    )   

if selected  == 'Data set':
    file_uploader = st.file_uploader("Upload your file ",['.csv'])
    
    @st.cache
    def dataset():
        df = pd.read_csv(file_uploader)
        st.write(df)
    pass



# *****************DATA Cleaning Process ***************************************************#
elif selected == 'Cleaning':
    file_uploader = st.file_uploader("Upload your file ",['.csv'])
    
    
    def dataset():
        df = pd.read_csv(file_uploader)
        return df
    df = dataset()
    st.write(df)
    opt = option_menu(
        menu_title = "Data set",
        options = ["Null Columns","Not Null Columns ","Descriptive statitics","Columns","Remove Columns","Deployment"],
        icons = ["house","book","envelope","book","house"],
        default_index = 0,
        orientation = "horizontal",
        styles = {
            
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "10px", "font-style":"Time new roman","text-align": "left", "margin":"0px", "--hover-color": "#eee"},
             "nav-link-selected": {"background-color": "black"},
        }
    )
    if opt == 'Null Columns':
        st.table(df.isnull().sum())
    if opt == "Not Null Columns":
       st.table(df.notnull().sum())
    if opt == "Descriptive statitics":
        st.table(df.describe())
    if opt == "Columns":
        st.table(df.columns)
    if opt == "Remove Columns":
        col = df.columns
        s = st.multiselect("Enter Column ",options = col)
        rem = st.button("Remove Column")
        if rem is True:
            df.drop(columns =s,inplace = True)
        st.write(df)
        choose = ["Rows","Columns"]
        remove_na = st.selectbox("Remove Null values ",options = choose)
        if remove_na == "Rows":
            st.write("Rows")
            if st.button("Remove "):
                df.dropna(axis=0,inplace = True)
                st.table(df.columns)
        else:
            st.write("Columns wise") 
            if st.button("Remove "):
                df.dropna(axis = 1,inplace = True)
                st.table(df.columns)
        
    
    

    
    
    
    
    
    
    
    
# ******************Exploratory Data Analysis ***********************************************#
elif selected == 'EDA':
    st.write("Hello Exploratory Data Analysis")
    file_uploader = st.file_uploader("Upload your file ",['.csv'])
    def dataset():
        df = pd.read_csv(file_uploader)
        return df
    df = dataset()
    st.write(df)
    if st.button("Exploratory Data Analysis"):
        pr = ProfileReport(df,explorative = True)
        st.header("Exploratory Data Analysis")
        st_profile_report(pr)
    if st.button("Exploratory Data Analysis "):
        st.header("Exploratory Data Analysis")
        AV = AutoViz_Class()
        AV.AutoViz(file_uploader)

    
    
  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#****************Machine Learning Algorthm*************************************************#
elif selected == 'Machine Learning':
    # st.write("Hello Machine Learning")
    with st.sidebar:
        opt = ["Linear Regression","Logistic Regression"]
        choose = st.selectbox("Choose Algorithm ",options= opt)
    if choose  == "Linear Regression":
            st.write("Perform Linear Regression")
            file_uploader = st.file_uploader("Upload your file ",['.csv'])
            df = pd.read_csv(file_uploader)
            st.write(df)
            if st.button("Check Information of Features "):
                pass
            opt = df.columns
            # Search engine
            select_independend_features = st.multiselect("Select Independent Features ",options = opt)
            # st.write(select_independend_features)
            select_target_feature = st.selectbox("Select Dependend feature ",options = opt)
            
            for i in select_independend_features:
                if i == select_target_feature:
                    st.warning("Cannot be  used Same features ")
                    break
                
            # Train and test splt
            st.subheader("Train and Test the data ")
            test_size = st.slider("Test Size ",0,100,30)
            Random_state = st.slider("Random State ",0,100,51)
            # Independend and  Dependend Features
            X = select_independend_features
            y = select_target_feature
            X_test,y_test,X_train,y_train  = train_test_split(X,y,test_size=0.2,random_state=51)
            

           
            # Machine learning follows the numerical data
            
          




          
# ******************************Dashboard*****************************************************#
# 1. Line Chart
# 2. Bar chart
# 3. Scatter plot
# 4. Pie Chart
# 5. Histogram
elif selected == 'Dashboard':
    file_uploader = st.file_uploader("Upload your file ",['.csv'])
    def dataset():
        df = pd.read_csv(file_uploader)
        return df
    df = dataset()
    st.write(df)
    st.write("Shape of dataset   : ",df.shape)
    # st.write("Information of dataset   : ",df.info)
 
 
    opt = [
            'Line Chart',
            'Bar Chart',
            'Area Chart',
            'Scatter Chart',
            'Column Chart',
            'Heatmap',
            'Pairplot'
    ]
    choose = st.sidebar.radio("Choose Chart  ",options= opt)
     
    if choose == 'Line Chart':
        #******************Line Chart *******************#
        st.header("Line Chart")
        opt = df.columns
        x= st.multiselect("Select X-axis ",options = opt)
        y = st.multiselect("Select Y-axis ",options = opt)
        if x == y:
            st.warning("Same columns ")
            
        st.header("Line Chart ")
        h = st.slider("Height of Line Chart ",100,500)
        if st.button("Line Chart"):
             st.line_chart(data=df, x=x, y=y,height = h)
        
    elif choose == "Bar Chart":
        opt = df.columns
        x= st.multiselect("Select X-axis ",options = opt)
        y = st.multiselect("Select Y-axis ",options = opt)
        if x == y:
            st.warning("Same columns ")
        h = st.slider("Height of Bar Chart ",100,500)
        if st.button("Bar Chart"):
             st.bar_chart(data= df,  x=x, y=y,height = h)

    elif choose == "Area Chart":
        # st.write("Bar chart")
        opt = df.columns
        x= st.multiselect("Select X  ",options = opt)
        y = st.multiselect("Select Y  ",options = opt)
        if x == y:
            st.warning("Same columns ")    
        st.header("Area Chart ")
        h = st.slider("Height of Line Chart ",100,500)
        if st.button("Area Chart "):
            st.area_chart(data=df,  x=x, y=y,  height=h,)
    elif choose == 'Scatter Chart':
        st.header("Scatter Plot")
        opt = df.columns
        x_col= st.selectbox("Select X  ",options = opt)
        y_col = st.selectbox("Select Y  ",options = opt)
        if x_col == y_col:
            st.warning("Same columns ")    
        col = st.selectbox("Choose Color Column ",options = opt)
        lst = ['aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance', 'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg', 'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl', 'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric', 'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys', 'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet', 'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges', 'orrd', 'oryel', 'oxy', 'peach', 'phase', 'picnic', 'pinkyl', 'piyg', 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn', 'puor', 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu', 'rdgy', 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar', 'spectral', 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn', 'tealrose', 'tempo', 'temps', 'thermal', 'tropic', 'turbid', 'turbo', 'twilight', 'viridis', 'ylgn', 'ylgnbu', 'ylorbr', 'ylorrd']
        colors = st.selectbox("Choose Color  ",options = lst)
        if st.button("Scatter Plot "):
            fig = px.scatter(
                    df,
                    x=x_col,
                    y=y_col,
                    color = col,
                    color_continuous_scale=colors,
                    
            )
            st.plotly_chart(fig, theme="streamlit", use_container_width=False)     
       
    elif choose == 'Column Chart':
        def country_group_callback():
            chosen_group = [
            group_name for group_name, selected in st.session_state.items() if
            selected and group_name in df.petal][0]
            countries = df.GROUPS_TO_COUNTRIES[chosen_group]
            st.session_state["default_countries"] = countries
        st.write("Or choose from predefined country group:")
        columns = st.columns(len(df.COUNTRY_GROUPS))
        for idx, column in enumerate(columns):
            with column:
                group = df.COUNTRY_GROUPS[idx]
                st.button(group, key=group, on_click=country_group_callback)
    elif choose == 'Heatmap':
        st.header("Line Chart")
        opt = df.columns
        x= st.multiselect("Select X-axis ",options = opt)
        
        if st.button("Heatmap"):    
            # st.header("Heatmap")
            # # fig, ax = plt.subplots()
            # fig = plt.subplots()
            # sns.heatmap(x.corr())
            # st.write(fig)
            pass

            
        
        
    else:
        st.write("Pairplot")
            
            
        
   
    



                    
# *****************************Deployment ***************************************************#
elif selected == 'Deployment':
    st.write("Hello Deployment")


# with st.sidebar.header("Navbars"):
#     file_uploader = st.file_uploader("Upload your file ",['.csv'])
   
# if file_uploader is not None:
#     df = pd.read_csv(file_uploader)
#     st.subheader("DATA SET")
#     st.write(df)
    


# opt = st.sidebar.multiselect("Enter your Option",['Cleaning','Exploratory Data Analysis','Machine Learning'])
    
# if opt == 'Cleaning':
#     st.write("New Tab")
# elif opt == 'Exploratory Data Analysis':
#     st.write("EDA")
# else:
#     st.write("ML")                 
   

#     # nav = st.radio("Select Option",options=["Data Cleaning","Exploratory Data Analysis ","Machine Learning"])
   
# # Options
# # loading the datasets

