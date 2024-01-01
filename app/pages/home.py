from dash import html

def display_homepage():
    '''
    Display the home page
    return: html div element
    '''
    return html.Div([
         html.Div([
            html.H1("Big Data in In-Flight Emergency Situations", 
                    className='slide-in-text'),            
        ]),
        html.Div([
            html.P("In-flight emergencies refer to unexpected situations or incidents that occur during an aircraft's flight, requiring immediate action to ensure the safety of the passengers, crew, and the aircraft itself. These emergencies can range from technical malfunctions to medical crises, severe weather encounters, fires, security threats, and more.",
                   className='home-p-description'),
            html.Br(),
            html.H4("Types of In-Flight Emergencies:", className='home-h4-description'),
            html.Br(),
            html.Br(),
            html.Ul([
                html.Li("Mechanical or Technical Failures: Issues with the aircraft's systems, engines, hydraulics, or other critical components."),
                html.Li("Medical Emergencies: Health-related issues experienced by passengers or crew members."),
                html.Li("Weather-Related Incidents: Turbulence, lightning strikes, severe storms, etc."),
                html.Li("Security Threats: Hijacking attempts, unruly passengers, suspicious activities, etc."),
                html.Li("Fire or Smoke: Onboard fires, electrical failures, or smoke detected in the cabin or cockpit.")
            ]),
            html.Br(),
            html.H4('Role of Big Data in Addressing In-flight Emergencies:'),
            html.Ul([
              html.Li("Predictive Maintenance: Big data analytics can help airlines predict potential technical failures by analyzing vast amounts of data from aircraft sensors, historical maintenance records, and flight data. This enables preemptive maintenance to reduce the likelihood of in-flight mechanical issues."),
              html.Li("Real-time Monitoring: Utilizing real-time data analytics, airlines can monitor flights and aircraft systems continuously. Any anomalies or deviations from normal operations can trigger immediate alerts, allowing for proactive responses and interventions."),
              html.Li("Enhanced Safety Measures: Big data analytics can assist in identifying safety trends and patterns, leading to the development of better safety protocols and procedures. Analyzing historical emergency data helps in devising more effective emergency response plans and training programs for flight crew"),
              html.Li("Efficient Resource Allocation: Analyzing big data can aid airlines in optimizing resource allocation during emergencies, such as directing emergency services, medical personnel, or supplies to the affected flight promptly."),
              html.Li("Passenger Health Monitoring: Airlines can utilize passenger data to monitor health conditions during flights. This information could be valuable in identifying potential medical emergencies early and providing timely assistance."),
              html.Li("Improving Incident Response: Big data analytics enables the collection and analysis of incident data from various sources, which can be used to improve incident response strategies, crisis management, and decision-making processes during emergencies."),
              html.Li("Post-Incident Analysis: After an in-flight emergency, detailed analysis of big data related to the incident helps in understanding the root causes, identifying areas for improvement, and implementing measures to prevent similar occurrences in the future.")
            ])
            
        ], className='inner-div-two-description')
    ], className='homepage-div')