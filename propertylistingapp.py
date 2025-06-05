import streamlit as st
import time
import datetime
from streamlit.logger import get_logger
#import  sqlalchemy.connector 
import pyodbc
import pandas as pd
import numpy as np

#from SessionState import _get_state
with open('mycss.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
LOGGER = get_logger(__name__)

#state = _get_state()

with open('mydatabase.txt') as datab:
    lines = datab.readlines()

# Get the number of lines read from the file
num_lines = len(lines)
i = 0
##
## in mydatabase.txt put below code
## pcsqlserver if sql server is used in pc
## pcmysql if mysql is used in pc
## pcpostgres if postgres is used in pc
## sqlserver if free server is used from free 
##  web site like somee.com where there is no auto increment
## mysql if free server is used for mysql
## 
mydatabase = lines[i].strip() #mydatabase = lines[i]
#st.write(mydatabase)

def run():
   # st.set_page_config(
        page_title="Property Listing Entry and Graphs"
        st.write(page_title)
   #    )
    

##st.write("Property Listing Entry and Graphs")

st.sidebar.success("Select from Below")

st.markdown(
        """
        ### Property Page Entry
        """
    )



# Using object notation
with st.sidebar.form("my_form"):
  add_selectbox = st.sidebar.selectbox(
    "What do you want to Do Now ?",
    ("Take from Here ","Deal with Customer Code","Add Property Listing", "View Listing", "Modify Listing","Add Customer Details","Modify Customer Details","Add Area and Place", "View Area and Place", "Modify Area and Place", "Add Property ,sub Property","View Property Types","Modify Property - Sub Property ")
  )

# Using "with" notation
  with st.sidebar:
    add_radio = st.radio(
        "Show Property from below",
        ("Latest (5 days)", "Last 15 days)", "Last 1 Month Old", "More than One Month")
    )
    add_property_selection = st.sidebar.selectbox(
        "Main Property ? ",
        ("Property Type ",'Flat','Bunglow','Twin Bunglow','Row House','Land')
        )
    
    add_sub_property_selection = st.sidebar.selectbox(
        "Sub Property ? ",
        ("Sub Property Type ",'1 BHK','2 BHK','3 BHK','4 BHK','5 BHK or More','Agricultural Land','Commercial Land','Both Type of Land','None')
        )
    
    add_area_selection_selection = st.sidebar.selectbox(
        "Select Area from Below ? ",
        ("Main Area :",'Andheri East','Andheri West','Vile Parle East','Vile Parle West')
        )
    
    add_sub_place_selection_selection = st.sidebar.selectbox(
        "Select Place / Pin Code ? ",
        ("Select place / pin code ", 'Andheri East Station' , 'Marol' ,'Juhu','None')
        )
    add_graph_type = st.radio(
        "Choose a Graph Type",
        ("Line Graph", "Bar Graph","Histogram","Pie Chart")
    )

    with st.sidebar:
       st.form_submit_button('Submit Selection', type="primary")



with st.spinner("Loading..."):
       time.sleep(1)
       st.write("")
st.sidebar.success("Done!")

if (add_selectbox == "Deal with Customer Code"):

    def init_connection():
        #st.write(mydatabase)
        if (mydatabase == "pcsqlserver"):  # pcsqlserver
           #st.write("i am here")
           return pyodbc.connect(
           "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
           + st.secrets["server"]
           + ";DATABASE="
           + st.secrets["database"]
           + ";UID="
           + st.secrets["username"]
           + ";PWD="
           + st.secrets["password"]
           )
    #st.write("h0")
    conn = init_connection()
    #st.write("h1")
    sql_qry = ""
    if (mydatabase=="pcsqlserver"):
       sql_qry = pd.read_sql_query("select customercode,customername,customercontactname from customertable",conn)
       df = pd.DataFrame(sql_qry,columns=['code','customer name','contact person'])
    ##st.dataframe(df.head(4), height=200)
      
       with st.container():       
         cols= st.columns(2)
         #cols[0], cols[1] = st.columns([3, 1])
         col1, col2 = st.columns([4, 1])
         #col1, col2 = st.columns([3, 1])
         #edit_btn = cols[1,3].button("✏️ Edit")  ## , key=f"edit_{index}")
         #delete_btn = cols[1,4].button("🗑️ Delete") ## , key=f"delete_{index}")
    
         with cols[0]: 
          
           with col1:
                  st.dataframe(df.reset_index(drop=True), height=200)  
                  st.markdown("### Actions")
                  edit_btn = st.button("✏️ Edit")
                  delete_btn = st.button("🗑️ Delete")

           #edit_btn = cols[1,3].button("✏️ Edit")  ## , key=f"edit_{index}")
           #delete_btn = cols[1,4].button("🗑️ Delete") ## , key=f"delete_{index}")

           # st.dataframe(df, height=200)
    ## st.table(df)
         with cols[1]:
           addcustomerform = st.form('mycustomeradd')
         with st.container():
            tab1,tab2,tab3= st.tabs(["Edit","Delete","Exit"])
            with tab1:
              st.dataframe(df.reset_index(drop=True), height=200) # st.dataframe(df, height=200)

if (add_selectbox == "View Property Types"):
   
     #@st.cache_resource
   
     def init_connection():
            return pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
            + st.secrets["server"]
            + ";DATABASE="
            + st.secrets["database"]
            + ";UID="
            + st.secrets["username"]
            + ";PWD="
            + st.secrets["password"]
            )

     conn = init_connection()
   
     def run_query1(query):
           with conn.cursor() as cur:
              cur.execute(query) 
              df=pd.DataFrame(cur.fetchall(),columns=["id","PropertyType","SubPropertytype"])
              st.table(df)
              return cur.fetchall()
          
     sql_qry = pd.read_sql_query("select id,propertytype,subpropertytype from propertyandsubproperty",conn)
     df = pd.DataFrame(sql_qry,columns=['id','propertytype','subpropertytype'])
     st.table(df)

     #rows = run_query("SELECT  * from propertyandsubproperty")
     
# Print results.
     #df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i 

     #df=pd.DataFrame(rows,columns=["id","PropertyType","SubPropertytype"])
     #for row in rows:
            #st.write(f"{row[0]} has a :{row[1]}:") 
     #st.table(df)

if (add_selectbox=="Add Property Listing"):
    propertylistingform = st.form('my_property_listing')
    
    start_date = propertylistingform.date_input('Enter start date', value=datetime.datetime(2023,12,23))
    area = propertylistingform.text_input('Your Area:','')
    place = propertylistingform.text_input('Your Place:', '')
    custcode = propertylistingform.text_input('Customer Code : ','Customer Code Please ? : ')
    #"""
    #num = st.number_input("Higher precision step", min_value=1.0, max_value=5.0, step=1e-6, format="%.5f")
    #"""
    expectedcost = propertylistingform.number_input('Likely Expected Cost ? : ')
    totalarea = propertylistingform.number_input('Total Area ? : ')
    measurementin = propertylistingform.selectbox('Measurement In ', ['Sq Ft','Meter','Inches','Cms'])
    typeofprop = propertylistingform.selectbox('Property Type', ['Flat','Bunglow','Twin Bunglow','Row House','Land'])
    subtypeprop = propertylistingform.selectbox('Sub Property Type', ['1 BHK','2 BHK','3 BHK','4 BHK','5 BHK or More','Agricultural Land','Commercial Land','Both Type of Land','None'])
    trantype = propertylistingform.selectbox('Transaction Type ', ['Buy','Sell','Rent','Leased ','Hire Purchase','Bank Dealing','None'])
    desc1 =  propertylistingform.text_area('Description : 1 : ')
    desc2 =  propertylistingform.text_area('Description : 2 : ')
    status1 = propertylistingform.selectbox('Status Type', ['OPEN','Appointment on','None'])
    status_date = propertylistingform.date_input('Enter status date', value=datetime.datetime(2023,12,23))
   
    submit = propertylistingform.form_submit_button('Accept Data', type="primary")
   
    if submit:
       propertylistingform.subheader('Saving Data')
    else:
       propertylistingform.subheader('&nbsp;')
       
if (add_selectbox=="Add Property ,sub Property"):
    propertytypeform = st.form('my_property_type',clear_on_submit=True)
    main_id = st.empty()
    main_id=""
    main_id = propertytypeform.number_input('Property ID','')
    main_property_type = st.empty()
    main_property_type=""
    main_property_type = propertytypeform.text_input('Property Type','')
    sub_property_type= st.empty()
    sub_property_type=""
    sub_property_type = propertytypeform.text_input('Sub Property Type ','')
    property_submit = propertytypeform.form_submit_button('Accept Property Type ',type="primary")
    if (property_submit):
        propertytypeform.subheader('Saving Property Type and Sub Type Details ')
        # line 1
        @st.cache_resource
        #myconn = sqlalchemy.connector.connect(host="localhost",user="sa",password="Myp@ssword",database="PropertyDatabase")
        #cur = myconn.cursor()  
        #@st.cache_data(ttl=600)
        # cursor=conn.cursor()
        
        
        
        
        

        # conn.execute("insert into propertyandsubproperty (propertytype,subpropertytype) values (" + "'" + main_property_type + "','" + sub_property_type+ "')")
      
        #conn.commit()
        def init_connection():
            return pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
            + st.secrets["server"]
            + ";DATABASE="
            + st.secrets["database"]
            + ";UID="
            + st.secrets["username"]
            + ";PWD="
            + st.secrets["password"]
            )

        conn = init_connection()
   
        def run_query(query):
           with conn.cursor() as cur:
              cur.execute(query)
             # propertytypeform.subheader('Saved Property Type and Sub Type Details Successfully... ')
              with st.spinner("Saved Data..."):
                 time.sleep(1)
                 st.write("")
              return (1) # cur.fetchall()

        rows = run_query("insert into propertyandsubproperty (id, propertytype,subpropertytype ) values (" + main_id + ",'" + main_property_type + "','" + sub_property_type+ "')")
        #run_query("SELECT * from propertylisting")
# Print results.
       # for row in rows:
       #     st.write(f"{row[0]} has a :{row[1]}:")
    
        # line end
    else:
        propertytypeform.subheader('&nbsp;')
        
       
        #propertytypeform.subheader('Saved Property Type and Sub Type Details Successfully... ')
   
#state.sync()    
    
if __name__=="__main__":
   run()