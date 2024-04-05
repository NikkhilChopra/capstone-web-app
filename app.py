import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import time 
import matplotlib.pyplot as plt


import psutil  

from Search_2D import env, env1, seafloorenv, warehouseenv, aircraftterrainenv, data1, agricultureenv, disasterenv, forestenv, pedestrainenv

from Search_2D.Anytime_D_Star import ADStar

from Search_2D.Bidirectional_a_star import BidirectionalAStar
from Search_2D.DStar import DStar
from Search_2D.LPAStar import LPAStar
from Search_2D.RTAAStar import RTAAStar
from Search_2D.plotting import Plotting 
from Meta_Heuristic_Algorithm.main import geneticAlgorithm
import altair as alt


def main():
    html_string = "<html><head><title>Yearly Symbol Prices</title></head><frameset><frame src='https://main--astonishing-flan-855511.netlify.app/?embedded=true'></frameset></html>"
    
    currentEnv = env


    # s_start=(10,5)
    # s_goal=(45,5)
    df = pd.read_csv("algo-analysis.csv")

    # toggle_button = st.sidebar.checkbox('Show only Analysis')
    # if(toggle_button):  
    #     analysis = st.sidebar.selectbox(
    #     'Choose Parameter to compare',
    #     ('Time of execution', 'CPU Usage', 'RAM Usage', 'Open and Closed list', 'Optimality'))

    #     if (analysis == 'Time of execution'):
    #         x = ['D* Algorithm', 'Bi-directional Algorithm', 'LPA* Algorithm', 'Anytime Repairing A* Algorithm', 'RTAA* Algorithm']
    #         y = [61, 6.5, 26, 300, 21]

    #         data = pd.DataFrame({'Algorithm': x, 'Time of execution': y})

    #         color_scale = alt.Scale(domain=x, range=['#FFCC33', '#66CCCC', '#FF9999', '#99CC99', '#FF6666'])

    #         chart = alt.Chart(data).mark_bar().encode(
    #             x=alt.X('Algorithm', sort='-y'),
    #             y=alt.Y('Time of execution', axis=alt.Axis(title='Time of execution')),
    #             color=alt.Color('Algorithm', scale=color_scale),
    #             tooltip=[alt.Tooltip('Algorithm'), alt.Tooltip('Time of execution', format=',d')]
    #         ).properties(
    #             title={
    #                 "text": " Time of executions v/s Algorithms",
    #                 "subtitle": "in ms",
    #                 "subtitleFontStyle": "italic",
    #                 "fontSize": 20,
    #                 "color": "gray"
    #             },
    #             width=600,
    #             height=600
    #         ).configure_axis(
    #             labelFontSize=14,
    #             titleFontSize=16,
    #             titleFontWeight='bold'
    #         ).configure_title(
    #             subtitleFontSize=16,
    #             subtitlePadding=10,
    #             subtitleColor='gray'
    #         )

    #         st.altair_chart(chart, use_container_width=True)

    #     if (analysis == 'CPU Usage'): 
    #         x = ['D* Algorithm', 'Bi-directional Algorithm', 'LPA* Algorithm', 'Anytime Repairing A* Algorithm', 'RTAA* Algorithm']
    #         y = [0.058, 0.01, 0.04, 2.06, 0.03]

    #         data = pd.DataFrame({'Algorithm': x, 'CPU Usage': y})

    #         color_scale = alt.Scale(domain=x, range=['#FCB711', '#F37021', '#CC004C', '#6460AA', '#008AB8'])

    #         chart = alt.Chart(data).mark_bar().encode(
    #             x=alt.X('CPU Usage', axis=alt.Axis(  title='CPU Usage')),
    #             y=alt.Y('Algorithm', sort='-x'),
    #             color=alt.Color('Algorithm', scale=color_scale),
    #             tooltip=[alt.Tooltip('Algorithm'), alt.Tooltip('CPU Usage', format='%')]
    #         ).properties(
    #             title={
    #                 "text": "CPU Usage v/s Algorithm",
    #                 "subtitle": "Percentage of CPU usage during execution",
    #                 "subtitleFontStyle": "italic",
    #                 "fontSize": 20,
    #                 "color": "gray"
    #             },
    #             width=600,
    #             height=600
    #         ).configure_axis(
    #             labelFontSize=14,
    #             titleFontSize=16,
    #             titleFontWeight='bold'
    #         ).configure_title(
    #             subtitleFontSize=16,
    #             subtitlePadding=10,
    #             subtitleColor='gray'
    #         )

    #         st.altair_chart(chart, use_container_width=True)

    #     if(analysis == 'RAM Usage'): 
    #         x = ['D* Algorithm', 'Bi-directional Algorithm', 'LPA* Algorithm', 'Anytime Repairing A* Algorithm', 'RTAA* Algorithm']
    #         y = [150, 155, 153, 162, 171]

    #         data = pd.DataFrame({'Algorithm': x, 'RAM Usage': y})

    #         color_scale = alt.Scale(domain=x, range=['#6b5b95', '#feb236', '#d64161', '#ff7b25', '#e5c5dd'])

    #         chart = alt.Chart(data).mark_bar().encode(
    #             x=alt.X('RAM Usage', axis=alt.Axis(title='RAM Usage (MB)')),
    #             y=alt.Y('Algorithm', sort='-x'),
    #             color=alt.Color('Algorithm', scale=color_scale),
    #             tooltip=[alt.Tooltip('Algorithm'), alt.Tooltip('RAM Usage', format='.1f', title='RAM Usage (MB)')]
    #         ).properties(
    #             title={
    #                 "text": "RAM Usage by Algorithm",
    #                 "subtitle": "Memory consumption during execution",
    #                 "subtitleFontStyle": "italic",
    #                 "fontSize": 20,
    #                 "color": "gray"
    #             },
    #             width=600,
    #             height=600
    #         ).configure_axis(
    #             labelFontSize=14,
    #             titleFontSize=16,
    #             titleFontWeight='bold'
    #         ).configure_title(
    #             subtitleFontSize=16,
    #             subtitlePadding=10,
    #             subtitleColor='gray'
    #         )

    #         st.altair_chart(chart, use_container_width=True)

    #     if(analysis == 'Open and Closed list'): 
    #         # Data
    #         x = ['D* Algorithm', 'Bi-directional Algorithm', 'LPA* Algorithm', 'Anytime Repairing A* Algorithm', 'RTAA* Algorithm']
    #         open_list_length = [587, 408, 467, 427, 487]
    #         closed_list_length = [3041, 2406, 2789, 2549, 2971]

    #         # Custom color palette
    #         color_palette = ['#5B8FF9', '#61DDAA', '#65789B', '#F6BD16', '#7262fd', '#78D3F8', '#9661BC', '#F6903D', '#008080']

    #         # Plot
    #         fig, ax = plt.subplots(figsize=(15, 13))
    #         ax.bar(x, open_list_length, color=color_palette[0], label='Open List Length')
    #         ax.bar(x, closed_list_length, bottom=open_list_length, color=color_palette[1], label='Closed List Length')
    #         ax.set_ylabel('Number of Nodes', fontsize=14, labelpad=12)
    #         ax.set_xlabel('Algorithm', fontsize=14, labelpad=12)
    #         ax.set_title('Search Space Explored by Algorithm', fontsize=18, pad=20, fontweight='bold')
    #         ax.legend(fontsize=12)

    #         # Styling
    #         ax.spines['top'].set_visible(False)
    #         ax.spines['right'].set_visible(False)
    #         ax.tick_params(axis='both', which='major', labelsize=12, length=0)
    #         ax.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)

    #         # Streamlit
    #         st.pyplot(fig)
        
    #     if(analysis == 'Optimality'):
    #         # Define the data
    #         data = pd.DataFrame({
    #             'Algorithm': ['D* Algorithm', 'Bi-directional Algorithm', 'LPA* Algorithm', 'Anytime Repairing A* Algorithm', 'RTAA* Algorithm'],
    #             'Path Length': [100, 95, 90, 95, 92]
    #         })

    #         # Define the chart
    #         chart = alt.Chart(data).mark_bar().encode(
    #             x=alt.X('Path Length', title='Path Length'),
    #             y=alt.Y('Algorithm', sort='-x', title='Algorithm'),
    #             color=alt.Color('Algorithm', scale=alt.Scale(scheme='dark2'), legend=None)
    #         ).properties(
    #             width=800,
    #             height=600,
    #             title='Optimality of Pathfinding Algorithms'
    #         )

    #         # Display the chart in Streamlit
    #         st.altair_chart(chart, use_container_width=True)
    #     return

    
    # geneticAlgorithmButton = st.sidebar.checkbox('Meta-heuristic Algorithm Demonstration');
    
    # if( geneticAlgorithmButton):
    #     geneticAlgorithm()
    #     if(st.button('Run simulation')):  
    #         components.html(html_string, height=800) 
    #     return  

    coordinates_input_s = st.sidebar.text_input('Enter start coordinates (X,Y)', value='0,0')
    coordinates_s = coordinates_input_s.split(',')

    obs_x_s = int(coordinates_s[0])
    obs_y_s = int(coordinates_s[1])

    coordinates_input_e = st.sidebar.text_input('Enter end coordinates (X,Y)', value='0,0')
    coordinates_e = coordinates_input_e.split(',')

    obs_x_e = int(coordinates_e[0])
    obs_y_e = int(coordinates_e[1])


    s_start = (obs_x_s, obs_y_s)
    s_goal = (obs_x_e, obs_y_e)

    option = st.sidebar.selectbox(
        'Choose heuristic algorithm',
        ('D* Algorithm', 'Bi-directional Algorithm',  'LPA* Algorithm', 'Anytime Repairing A* Algorithm', 'RTAA* Algorithm'))
    
    if option != 'Genetic Algorithm': 
        environments = st.sidebar.selectbox(
            'Choose environment',
            ('Data1', 'Aircraft Stealth Mission Terrain', 'Agriculture Terrain', 'Extra Terrestrial Terrain', 'Elevated rocky terrain', 'Seafloor Terrain', 'Industry Warehouse Terrain', 'Earthquake Disaster Terrain', 'Forest Terrain', 'City street Terrain'))

        if environments == 'Aircraft Stealth Mission Terrain':
            # s_start = (10, 3)
            # s_goal = (35, 2)
            currentEnv = aircraftterrainenv
            html = '<html><body><img style="margin-bottom: 10px;" src="https://raw.githubusercontent.com/Apurva-tech/files/master/aircraftTerrain.jpeg" alt="Aircraft" width="300" height="150"></body></html>'
            st.sidebar.metric(label="Best algorithm", value="RTAA* Algorithm", delta="optimal, time efficient")
            st.sidebar.markdown(html, unsafe_allow_html=True)
            if(st.sidebar.button('Show RTAA*')): 
                option = 'RTAA* Algorithm'


        elif environments == 'Agriculture Terrain':
            s_start = (2, 2)
            s_goal = (48, 2)
            currentEnv = agricultureenv
            html = '<html><body><img style="margin-bottom: 10px;" src="https://media.istockphoto.com/id/454184549/photo/soybean-field.jpg?s=612x612&w=0&k=20&c=pRJJFvHnsjnEfkQRW5s-hKS-PGtYfdcrh7mWzQWdvM0=" alt="Agriculture" width="300" height="150"></body></html>'
            st.sidebar.metric(label="Best algorithm", value="Bidirectional A* Algorithm", delta="optimality, slowly changing environment")
            st.sidebar.markdown(html, unsafe_allow_html=True)
            if(st.sidebar.button('Show Bidirectional')): 
                option = 'Bi-directional Algorithm'
        
        elif environments == 'Data1':
            s_start = (2, 1)
            s_goal = (12, 10)
            currentEnv = data1
            html = '<html><body><img style="margin-bottom: 10px;" src="https://media.istockphoto.com/id/454184549/photo/soybean-field.jpg?s=612x612&w=0&k=20&c=pRJJFvHnsjnEfkQRW5s-hKS-PGtYfdcrh7mWzQWdvM0=" alt="Agriculture" width="300" height="150"></body></html>'
            st.sidebar.metric(label="Best algorithm", value="Bidirectional A* Algorithm", delta="optimality, slowly changing environment")
            st.sidebar.markdown(html, unsafe_allow_html=True)
            if(st.sidebar.button('Show Bidirectional')): 
                option = 'Bi-directional Algorithm'

        elif environments == 'Extra Terrestrial Terrain':
            s_start = (1, 1)
            s_goal = (42, 29)
            currentEnv = env
            html = '<html><body><img style="margin-bottom: 10px;" src="https://www.vaisala.com/sites/default/files/styles/16_9_liftup_extra_large/public/images/LIFT-Mars_3D-illustration_1600x900.jpg" alt="Extra Terrestrial Terrain" width="300" height="150"></body></html>'
            st.sidebar.metric(label="Best algorithm", value="D* or RTAA* Algorithm", delta="fuel efficient: optimum time and space complexity")
            st.sidebar.markdown(html, unsafe_allow_html=True)
            if(st.sidebar.button('Show RTAA*')): 
                option = 'RTAA* Algorithm'

        elif environments == 'Elevated rocky terrain':
            currentEnv = env1
            html = '<html><body><img style="margin-bottom: 10px;" src="https://developers.google.com/static/maps/documentation/gaming/images/elevation2.png" alt="Elevated rocky terrain" width="300" height="150"></body></html>'
            st.sidebar.metric(label="Best algorithm", value="ARA* Algorithm", delta="dynamic env")
            st.sidebar.markdown(html, unsafe_allow_html=True)
            if(st.sidebar.button('Show ARA*')): 
                option = 'Anytime Repairing A* Algorithm'

        elif environments == 'Seafloor Terrain':
            currentEnv = seafloorenv
            html = '<html><body><img style="margin-bottom: 10px;" src="https://cdna.artstation.com/p/assets/images/images/003/214/442/large/anil-isbilir-highresscreenshot00002-copy.jpg" alt="Seafloor Terrain" width="300" height="150"></body></html>'
            st.sidebar.metric(label="Best algorithm", value="D* Algorithm", delta="optimal, complex environments")
            st.sidebar.markdown(html, unsafe_allow_html=True)
            if(st.sidebar.button('Show D*')): 
                option = 'D* Algorithm'

        elif environments == 'Earthquake Disaster Terrain':
            s_start = (2, 2)
            s_goal = (48, 2)
            currentEnv = disasterenv
            html = '<html><body><img style="margin-bottom: 10px;" src="https://1.bp.blogspot.com/-977hjZn3njU/WRBW1DBF_LI/AAAAAAAAMRM/EYnfV9xuT4knm2REBExZeANvu67cooB6wCLcB/s1600/The%2Bdramatic%2Bterrain%2B-%2Bthe%2Bjoin%2Bbetween%2Btwo%2Btectonic%2Bplates.jpg" alt="Earthquake Disaster Terrain" width="300" height="150"></body></html>'
            st.sidebar.metric(label="Best algorithm", value="D* Algorithm", delta="time, memory efficient")
            st.sidebar.markdown(html, unsafe_allow_html=True)
            if(st.sidebar.button('Show D*')): 
                option = 'D* Algorithm'

        elif environments == 'Industry Warehouse Terrain':
            s_start = (5, 5)
            s_goal = (45, 25)
            currentEnv = warehouseenv
            html = '<html><body><img style="margin-bottom: 10px;" src="https://www.360connect.com/wp-content/uploads/2020/12/forklift-835340_1920.jpg" alt="Industry Warehouse Terrain" width="300" height="150"></body></html>'
            st.sidebar.metric(label="Best algorithm", value="LPA* Algorithm", delta="slow changing env, optimal")
            st.sidebar.markdown(html, unsafe_allow_html=True)
            if(st.sidebar.button('Show LPA*')): 
                option = 'LPA* Algorithm'

        elif environments == 'Forest Terrain':
            s_start = (5, 25)
            currentEnv = forestenv
            html = '<html><body><img style="margin-bottom: 10px;" src="https://img5.goodfon.com/wallpaper/nbig/0/cb/priroda-leto-vid-sverkhu-les-derevia-doroga.jpg" alt="Forest Terrain" width="300" height="150"></body></html>'
            st.sidebar.metric(label="Best algorithm", value="LPA* Algorithm", delta="optimal, less time complexity")
            st.sidebar.markdown(html, unsafe_allow_html=True)
            if(st.sidebar.button('Show LPA*')): 
                option = 'LPA* Algorithm'

        elif environments == 'City street Terrain':
            s_start = (2, 2)
            s_goal = (43, 37)
            currentEnv = pedestrainenv
            html = '<html><body><img style="margin-bottom: 10px;" src="https://community.esri.com/legacyfs/online/121677_3.jpg" alt="City street Terrain" width="300" height="150"></body></html>'
            st.sidebar.metric(label="Best algorithm", value="Bidirectional A* Algorithm", delta="time, accurate")
            st.sidebar.markdown(html, unsafe_allow_html=True)
            if(st.sidebar.button('Show Bidirectional')): 
                option = 'Bi-directional Algorithm'

  
    obs = []
    if (option == 'D* Algorithm'):
        # obs_x = st.sidebar.slider('Choose an obstacle (X)', 0, 51, 0)
        # obs_y = st.sidebar.slider('Choose an obstacle (Y)', 0, 31, 0)
        obs_x = st.sidebar.number_input('Enter obstacle (X)', min_value=0, max_value=51, value=0, step=1)
        obs_y = st.sidebar.number_input('Enter obstacle (Y)', min_value=0, max_value=51, value=0, step=1)
        st.write("Added obstacles at: ", "(X ", obs_x, ', Y', obs_y, ')')

        obs = [obs_x, obs_y]
        dstar = DStar(s_start, s_goal, currentEnv)
        dstar.run(s_start, s_goal, obs)
        show_anim = st.checkbox('Run Animation')
        if(show_anim): 
            if(environments == 'Aircraft Stealth Mission Terrain'):
                st.video('gif/d_star/aircraft.mp4', format="video/mp4", start_time=0)
            elif environments == 'Agriculture Terrain':
                st.video('gif/d_star/agriculture.mp4', format="video/mp4", start_time=0)
            elif environments == 'Extra Terrestrial Terrain':
                st.video('gif/d_star/extraTerres.mp4', format="video/mp4", start_time=0)
            elif environments == 'Elevated rocky terrain':
                st.video('gif/d_star/elevatedRocky.mp4', format="video/mp4", start_time=0)
            elif environments == 'Seafloor Terrain':
                st.video('gif/d_star/seafloor.mp4', format="video/mp4", start_time=0)
            elif environments == 'Earthquake Disaster Terrain':
                st.video('gif/d_star/earthquake.mp4', format="video/mp4", start_time=0)
            elif environments == 'Industry Warehouse Terrain':
                st.video('gif/d_star/industry.mp4', format="video/mp4", start_time=0)
            elif environments == 'Forest Terrain':
                st.video('gif/d_star/forest.mp4', format="video/mp4", start_time=0)
            elif(environments == 'City street Terrain'):
                st.video('gif/d_star/pedestrian.mp4', format="video/mp4", start_time=0)
        

    elif option == 'Bi-directional Algorithm':
        start = time.time()
        bastar = BidirectionalAStar(s_start, s_goal, "euclidean", currentEnv)
        plot = Plotting(s_start, s_goal, currentEnv)
        path, visited_fore, visited_back = bastar.searching()
        end = time.time()

        successMessage = ' ⌛ Time of execution of Bidirectional A* algorithm: ' + \
            str(round((end-start) * 10**3, 6)) + ' ms'
        st.sidebar.success(successMessage)
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_time = end - start
        cpu = '💻 CPU usage: ' + str(round(cpu_time * cpu_percent / psutil.cpu_count(), 6)) + ' %'
        st.sidebar.success(cpu)
        process = psutil.Process()
        ram_usage = round(process.memory_info().rss / 1024 / 1024, 6)
        ram = '💽 RAM usage: ' + str(ram_usage) + ' MB'
        st.sidebar.success(ram)

        plot.animation_bi_astar(
            path, visited_fore, visited_back, "Bidirectional-A*")
        
        show_anim = st.checkbox('Run Animation')
        if(show_anim): 
            if(environments == 'Aircraft Stealth Mission Terrain'):
                st.video('gif/bi_astar/aircraft.mp4', format="video/mp4", start_time=0)
            elif environments == 'Agriculture Terrain':
                st.video('gif/bi_astar/agriculture.mp4', format="video/mp4", start_time=0)
            elif environments == 'Extra Terrestrial Terrain':
                st.video('gif/bi_astar/extraTerres.mp4', format="video/mp4", start_time=0)
            elif environments == 'Elevated rocky terrain':
                st.video('gif/bi_astar/elevatedRocky.mkv', format="video/mkv", start_time=0)
            elif environments == 'Seafloor Terrain':
                st.video('gif/bi_astar/seafloor.mkv', format="video/mkv", start_time=0)
            elif environments == 'Earthquake Disaster Terrain':
                st.video('gif/bi_astar/earthquake.mkv', format="video/mkv", start_time=0)
            elif environments == 'Industry Warehouse Terrain':
                st.video('gif/bi_astar/industry.mkv', format="video/mkv", start_time=0)
            elif environments == 'Forest Terrain':
                st.video('gif/bi_astar/forest.mkv', format="video/mkv", start_time=0)
            elif(environments == 'City street Terrain'):
                st.video('gif/bi_astar/pedestrian.mp4', format="video/mp4", start_time=0)
        
    
    elif option == 'LPA* Algorithm':
        lpastar = LPAStar(s_start, s_goal, "Euclidean", currentEnv)
        lpastar.run()
        show_anim = st.checkbox('Run Animation')
        if(show_anim): 
            if(environments == 'Aircraft Stealth Mission Terrain'):
                st.video('gif/lpa_star/aircraft.mkv', format="video/mkv", start_time=0)
            elif environments == 'Agriculture Terrain':
                st.video('gif/lpa_star/agriculture.mkv', format="video/mkv", start_time=0)
            elif environments == 'Extra Terrestrial Terrain':
                st.video('gif/lpa_star/extraTerres.mkv', format="video/mkv", start_time=0)
            elif environments == 'Elevated rocky terrain':
                st.video('gif/lpa_star/elevatedRocky.mkv', format="video/mkv", start_time=0)
            elif environments == 'Seafloor Terrain':
                st.video('gif/lpa_star/seafloor.mkv', format="video/mkv", start_time=0)
            elif environments == 'Earthquake Disaster Terrain':
                st.video('gif/lpa_star/earthquake.mkv', format="video/mkv", start_time=0)
            elif environments == 'Industry Warehouse Terrain':
                st.video('gif/lpa_star/industry.mkv', format="video/mkv", start_time=0)
            elif environments == 'Forest Terrain':
                st.video('gif/lpa_star/forest.mkv', format="video/mkv", start_time=0)
            elif(environments == 'City street Terrain'):
                st.video('gif/lpa_star/pedestrian.mkv', format="video/mkv", start_time=0)
        

    elif option == 'Anytime Repairing A* Algorithm':
        dstar = ADStar(s_start, s_goal, 2.5, "euclidean", currentEnv)
        dstar.run()
        show_anim = st.checkbox('Run Animation')
        if(show_anim): 
            if(environments == 'Aircraft Stealth Mission Terrain'):
                st.video('gif/anytime_dstar/aircraft.mkv', format="video/mkv", start_time=0)
            elif environments == 'Agriculture Terrain':
                st.video('gif/anytime_dstar/agriculture.mkv', format="video/mkv", start_time=0)
            elif environments == 'Extra Terrestrial Terrain':
                st.video('gif/anytime_dstar/extraTerres.mkv', format="video/mkv", start_time=0)
            elif environments == 'Elevated rocky terrain':
                st.video('gif/anytime_dstar/elevatedRocky.mkv', format="video/mkv", start_time=0)
            elif environments == 'Seafloor Terrain':
                st.video('gif/anytime_dstar/seafloor.mkv', format="video/mkv", start_time=0)
            elif environments == 'Earthquake Disaster Terrain':
                st.video('gif/anytime_dstar/earthquake.mkv', format="video/mkv", start_time=0)
            elif environments == 'Industry Warehouse Terrain':
                st.video('gif/anytime_dstar/industry.mkv', format="video/mkv", start_time=0)
            elif environments == 'Forest Terrain':
                st.video('gif/anytime_dstar/forest.mkv', format="video/mkv", start_time=0)
            elif(environments == 'City street Terrain'):
                st.video('gif/anytime_dstar/pedestrian.mkv', format="video/mkv", start_time=0)
        

    elif option == 'RTAA* Algorithm':
        if environments == 'Elevated rocky terrain':
            st.video('gif/rtaa_star/elevatedRocky.mkv', format="video/mkv", start_time=0)
            return
        start = time.time()
        rtaa = RTAAStar(s_start, s_goal, 240, "euclidean", currentEnv)
        plot = Plotting(s_start, s_goal, currentEnv)
        rtaa.searching()
        end = time.time()
        successMessage = ' ⌛ Time of execution of Real-time Adaptive A* (RTAA*) algorithm: ' + \
            str(round((end-start) * 10**3, 6)) + ' ms'
        st.sidebar.success(successMessage)
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_time = end - start
        cpu = '💻 CPU usage: ' + str(round(cpu_time * cpu_percent / psutil.cpu_count(), 6)) + ' %'
        st.sidebar.success(cpu)
        process = psutil.Process()
        ram_usage = round(process.memory_info().rss / 1024 / 1024, 6)
        ram = '💽 RAM usage: ' + str(ram_usage) + ' MB'
        st.sidebar.success(ram)

        plot.animation_lrta(rtaa.path, rtaa.visited,
                            "Real-time Adaptive A* (RTAA*)")
         
        show_anim = st.checkbox('Run Animation')
        if(show_anim): 
            if(environments == 'Aircraft Stealth Mission Terrain'):
                st.video('gif/rtaa_star/aircraft.mkv', format="video/mkv", start_time=0)
            elif environments == 'Agriculture Terrain':
                st.video('gif/rtaa_star/agriculture.mkv', format="video/mkv", start_time=0)
            elif environments == 'Extra Terrestrial Terrain':
                st.video('gif/rtaa_star/extraTerres.mkv', format="video/mkv", start_time=0)
            elif environments == 'Elevated rocky terrain':
                st.video('gif/rtaa_star/elevatedRocky.mkv', format="video/mkv", start_time=0)
            elif environments == 'Seafloor Terrain':
                st.video('gif/rtaa_star/seafloor.mkv', format="video/mkv", start_time=0)
            elif environments == 'Earthquake Disaster Terrain':
                st.video('gif/rtaa_star/earthquake.mkv', format="video/mkv", start_time=0)
            elif environments == 'Industry Warehouse Terrain':
                st.video('gif/rtaa_star/industry.mkv', format="video/mkv", start_time=0)
            elif environments == 'Forest Terrain':
                st.video('gif/rtaa_star/forest.mkv', format="video/mkv", start_time=0)
            elif(environments == 'City street Terrain'):
                st.video('gif/rtaa_star/pedestrian.mkv', format="video/mkv", start_time=0)
        

    if option != 'Genetic Algorithm':
      st.table(df)
    


if __name__ == '__main__':
    main()
