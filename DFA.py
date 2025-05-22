import streamlit as st
import graphviz
import time
import streamlit.components.v1 as components
from PIL import Image


# --- DFA class ---
class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False  # invalid symbol
            current_state = self.transition_function.get((current_state, symbol))
            if current_state is None:
                return False  # no valid transition
        return current_state in self.accept_states

def simulate_dfa(dfa, input_string):
    """Simulate DFA step-by-step and collect transitions."""
    current_state = dfa.start_state
    path = [(current_state, None)]  # list of (state, symbol)

    for symbol in input_string:
        if symbol not in dfa.alphabet:
            return path, False, f"Invalid symbol '{symbol}'"
        
        next_state = dfa.transition_function.get((current_state, symbol))
        if next_state is None:
            return path, False, f"No transition from {current_state} on '{symbol}'"

        path.append((next_state, symbol))
        current_state = next_state

    accepted = current_state in dfa.accept_states
    return path, accepted, None
    
def draw_dfa(dfa, active_state=None):
    """Draw the DFA highlighting the active_state."""
    dot = graphviz.Digraph(engine='dot')  # Use 'dot' for horizontal layout
    
    # Set graph attributes for better horizontal layout with fixed zoom
    base_size = 30
    zoom_factor = 0.50  # Fixed zoom level
    zoomed_size = base_size * zoom_factor
    dot.attr(rankdir='LR', size=f'{zoomed_size},{zoomed_size/3}', dpi='73', splines='true')
    dot.attr('node', shape='circle', style='filled', fillcolor='white', 
             fontname='Arial', fontsize=str(20 * zoom_factor), width=str(1 * zoom_factor), height=str(1 * zoom_factor),
             margin='0.2', penwidth='2')
    dot.attr('edge', fontname='Arial', fontsize=str(20 * zoom_factor), penwidth='1.2')

    # Draw nodes
    for state in dfa.states:
        if state in dfa.accept_states:
            if state == active_state:
                dot.node(state, shape="doublecircle", style="filled", 
                        fillcolor="green", color="darkgreen", fontcolor="black", penwidth='2.5')
            else:
                dot.node(state, shape="doublecircle", style="filled", 
                        fillcolor="white", color="darkgreen", penwidth='2.5')
        else:
            if state == active_state:
                dot.node(state, style="filled", fillcolor="green", 
                        color="darkgreen", fontcolor="black", penwidth='2.5')
            else:
                dot.node(state, style="filled", fillcolor="white", 
                        color="darkgreen", penwidth='1.5')

    # Start arrow with custom styling
    dot.node("start", shape="none", label="")
    dot.edge("start", dfa.start_state, penwidth='1.5')

    # Draw edges with curved arrows and better spacing
    for (from_state, symbol), to_state in dfa.transition_function.items():
        if from_state == to_state:
            # Self-loop
            dot.edge(from_state, to_state, label=symbol, 
                    constraint='false', penwidth='1.2')
        else:
            dot.edge(from_state, to_state, label=symbol, 
                    constraint='true', penwidth='1.2')

    return dot
def draw_input_pointer(input_string, position):
    """Draw input string with a moving pointer ^."""
    spaced_input = '  '.join(input_string)
    pointer = '   ' * position + '^'
    return spaced_input + "\n" + pointer
    

# --- DFA definition: all states and transitions filled (best-effort from image) ---
states = {
    'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20','q21', 'qF'
}
alphabet = {'a', 'b'}

transition_function = {}

# By default, all transitions go to q_dead


# Fill in actual transitions (best-effort from your DFA image)
transition_function[('q0', 'a')] = 'q1'
transition_function[('q0', 'b')] = 'q2'

transition_function[('q1', 'a')] = 'q3'
transition_function[('q1', 'b')] = 'q2'
transition_function[('q2', 'a')] = 'q1'
transition_function[('q2', 'b')] = 'q3'
transition_function[('q3', 'a')] = 'q4'
transition_function[('q3', 'b')] = 'q5'
transition_function[('q4', 'a')] = 'q3'
transition_function[('q5', 'b')] = 'q3'
transition_function[('q4', 'b')] = 'q6'
transition_function[('q5', 'a')] = 'q7'
transition_function[('q6', 'a')] = 'q8'
transition_function[('q6', 'b')] = 'q10'
transition_function[('q7', 'a')] = 'q9'
transition_function[('q7', 'b')] = 'q10'
transition_function[('q8', 'a')] = 'q9'
transition_function[('q8', 'b')] = 'q10'
transition_function[('q9', 'a')] = 'q17'
transition_function[('q9', 'b')] = 'q12'
transition_function[('q10', 'a')] = 'q11'
transition_function[('q10', 'b')] = 'q11'
transition_function[('q11', 'a')] = 'q9'
transition_function[('q11', 'b')] = 'q13'
transition_function[('q12', 'a')] = 'q13'
transition_function[('q12', 'b')] = 'q11'
transition_function[('q13', 'a')] = 'q14'
transition_function[('q13', 'b')] = 'q15'
transition_function[('q14', 'a')] = 'q17'
transition_function[('q14', 'b')] = 'q16'
transition_function[('q15', 'a')] = 'q14'
transition_function[('q15', 'b')] = 'q17'
transition_function[('q16', 'a')] = 'q17'
transition_function[('q16', 'b')] = 'q17'
transition_function[('q17', 'a')] = 'q18'
transition_function[('q17', 'b')] = 'q19'
transition_function[('q18', 'a')] = 'q20'
transition_function[('q18', 'b')] = 'q19'
transition_function[('q19', 'a')] = 'q21'
transition_function[('q19', 'b')] = 'q20'
transition_function[('q20', 'b')] = 'q19'
transition_function[('q20', 'a')] = 'qF'
transition_function[('q21', 'a')] = 'q20'
transition_function[('q21', 'b')] = 'qF'
transition_function[('qF', 'a')] = 'qF'
transition_function[('qF', 'b')] = 'qF'


start_state = 'q0'
accept_states = {'qF'}

dfa = DFA(states, alphabet, transition_function, start_state, accept_states)

# --- DFA definitions ---
# DFA for (a and b)
states_ab = states
alphabet_ab = alphabet
transition_function_ab = transition_function
start_state_ab = start_state
accept_states_ab = accept_states

dfa_ab = DFA(states_ab, alphabet_ab, transition_function_ab, start_state_ab, accept_states_ab)

# DFA for (0 and 1) -- simple example, you can expand as needed
states_01 = {'s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16', 's17', 's18', 's19', 's20', 's21', 's22', 's23', 's24', 's25','s26','s27', 's28', 's29',"s30", 's31', 'sF'}
alphabet_01 = {'0', '1'}
transition_function_01 = {
    ('s0', '0'): 's2',
    ('s0', '1'): 's1',
    ('s1', '0'): 's3',
    ('s1', '1'): 's6',
    ('s2', '0'): 's4',
    ('s2', '1'): 's5',
    ('s3', '0'): 's4',
    ('s3', '1'): 's7',
    ('s4', '0'): 's12',
    ('s4', '1'): 's8',
    ('s5', '0'): 's9',
    ('s5', '1'): 's6',
    ('s6', '0'): 's11',
    ('s6', '1'): 's10',
    ('s7', '0'): 's10',
    ('s7', '1'): 's10',
    ('s8', '0'): 's16',
    ('s8', '1'): 's15',
    ('s9', '0'): 's12',
    ('s9', '1'): 's10',
    ('s10', '0'): 's15',
    ('s10', '1'): 's15',
    ('s11', '0'): 's15',
    ('s11', '1'): 's13',
    ('s12', '0'): 's15',
    ('s12', '1'): 's21',
    ('s13', '0'): 's14',
    ('s13', '1'): 's18',
    ('s14', '0'): 's26',
    ('s14', '1'): 's15',
    ('s15', '0'): 's19',
    ('s15', '1'): 's15',
    ('s16', '0'): 's17',
    ('s16', '1'): 's20',
    ('s17', '0'): 's26',
    ('s17', '1'): 's21',
    ('s18', '0'): 's25',
    ('s18', '1'): 's24',
    ('s19', '0'): 's26',
    ('s19', '1'): 's18',
    ('s20', '0'): 's23',
    ('s20', '1'): 's23',
    ('s21', '0'): 's22',
    ('s21', '1'): 's18',
    ('s22', '0'): 's26',
    ('s22', '1'): 's20',
    ('s23', '0'): 's19',
    ('s23', '1'): 's27',
    ('s24', '0'): 's25',
    ('s24', '1'): 's27',
    ('s25', '0'): 's26',
    ('s25', '1'): 's27',
    ('s26', '0'): 's27',
    ('s26', '1'): 's18',
    ('s27', '0'): 's28',
    ('s27', '1'): 's30',
    ('s28', '0'): 's31',
    ('s28', '1'): 's30',
    ('s29', '0'): 's31',
    ('s29', '1'): 'sF',
    ('s30', '0'): 's31',
    ('s30', '1'): 's29',
    ('s31', '0'): 'sF',
    ('s31', '1'): 'sF',
    ('sF', '0'): 'sF',
    ('sF', '1'): 'sF',
    



}

start_state_01 = 's0'
accept_states_01 = {'sF'}  # Make sure 'TRAP' is not in accept states
dfa_01 = DFA(states_01, alphabet_01, transition_function_01, start_state_01, accept_states_01)

# --- Streamlit UI ---
st.set_page_config(page_title="DFA Compiler & Visualizer", layout="wide")

# Create tabs
tab1, tab2, tab3 = st.tabs(["DFA Visualization","CFG", "PDA Visualization"])

with tab1:
    # Language selection
    dfa_language = st.selectbox(
        "Select DFA Language:",
        ["(a and b)", "(0 and 1)"]
    )

    if dfa_language == "(a and b)":
        dfa = dfa_ab
        alphabet = alphabet_ab
        dfa_title = "🌟 DFA Compiler & Visualizer (a and b)"
        dfa_pattern = "This DFA matches the pattern: (a+b)\*(aa+bb)(aa+bb)\*(ab+ba+aba)(bab+aba+bbb)(a+b+aa+bb)\*(bb+aa+aba)(aaa+bba+bab)(aaa+bba+bab)\*"
        st.sidebar.title("Valid String Examples")
        st.sidebar.code("""
        aabbaa
        bbabab
        aababab
        """)
    else:
        dfa = dfa_01
        alphabet = alphabet_01
        dfa_title = "🌟 DFA Compiler & Visualizer (0 and 1)"
        dfa_pattern = "This DFA matches the pattern:(1+0)\*(11+00+101+010)(11+00)\*(11+00+0+1)(1+0+11)(11+00)\*(101+000+111)(1+0)\*(101+000+111+001+100)(11+00+1+0)"
        st.sidebar.title("Valid String Examples")
        st.sidebar.code("""
        110011
        0010101
        01011
        """)

    st.title(dfa_title)
    st.write(dfa_pattern)

    # DFA Visualization (top, always visible)
    dfa_placeholder = st.empty()
    dfa_placeholder.graphviz_chart(draw_dfa(dfa))

    st.subheader("Test Multiple Strings")
    # Single input field for comma-separated strings
    test_inputs = st.text_input("Enter strings (comma-separated):", key="comma_separated_inputs")
    
    if test_inputs:
        # Split the input string by commas and strip whitespace
        input_strings = [s.strip() for s in test_inputs.split(',')]
        
        # Process each string and display results
        for idx, test_input in enumerate(input_strings):
            if test_input:  # Only process non-empty strings
                path, accepted, error = simulate_dfa(dfa, test_input)
                
                # Create a container for each result
                result_container = st.container()
                with result_container:
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        # Display the input string with appropriate styling
                        if error or not accepted:
                            st.markdown(f"**Input {idx+1}:** {test_input} <span style='color: red;'>❌</span>", unsafe_allow_html=True)
                            if error:
                                st.error(f"Error: {error}")
                            else:
                                st.error(f"String rejected")
                        else:
                            st.markdown(f"**Input {idx+1}:** {test_input} <span style='color: green;'>✅</span>", unsafe_allow_html=True)
                            st.success(f"String accepted")
                    
                    with col2:
                        # Add simulation button
                        sim_key = f"sim_button_{idx}"
                        if st.button(f"Simulate", key=sim_key):
                            if error:
                                st.error(f"Error: {error}")
                            else:
                                st.write("### Step-by-Step DFA Simulation:")
                                input_placeholder = st.empty()  # for the input string and pointer
                                
                                # Update the main visualization for each step
                                for step_idx, (state, symbol) in enumerate(path):
                                    # Update the main visualization
                                    dfa_placeholder.graphviz_chart(draw_dfa(dfa, active_state=state))
                                    
                                    # show input string with moving pointer
                                    with input_placeholder.container():
                                        if step_idx == 0:
                                            input_pos = 0
                                        else:
                                            input_pos = step_idx - 1  # because path has an extra initial start state
                                        st.code(draw_input_pointer(test_input, input_pos), language="markdown")
                                        if step_idx == 0:
                                            st.write(f"Start at state **{state}**")
                                        else:
                                            st.write(f"Read **'{symbol}'**, move to state **{state}**")
                                    time.sleep(1.2)
                                
                                # Reset the visualization after simulation
                                dfa_placeholder.graphviz_chart(draw_dfa(dfa))
                                
                                if accepted:
                                    st.success(f"The string '{test_input}' is **ACCEPTED** by the DFA! 🎉")
                                else:
                                    st.error(f"The string '{test_input}' is **REJECTED** by the DFA. ❌")
                                
                                # Add Close Simulation button
                                close_key = f"close_button_{idx}"
                                if st.button("Close Simulation", key=close_key):
                                    input_placeholder.empty()
                                    dfa_placeholder.graphviz_chart(draw_dfa(dfa))

with tab2:
    st.title("Context-Free Grammar (CFG) Visualization")
    
    
    # Add dropdown for CFG selection
    cfg_language = st.selectbox(
        "Select CFG Pattern:",
        ["(a and b)", "(0 and 1)"],
        key="cfg_language"
    )
    
    if cfg_language == "(a and b)":
        st.write("Context-Free Grammar for (a and b) pattern")
        try:
            cfg_image = Image.open("cfg_a&b.jpg")
            st.image(cfg_image, caption="CFG Diagram for (a and b)", use_container_width=True)
        except Exception as e:
            st.error(f"Error loading CFG image: {str(e)}")
    else:
        st.write("Context-Free Grammar for (0 and 1) pattern")
        try:
            cfg_image = Image.open("cfg1_0.jpg")
            st.image(cfg_image, caption="CFG Diagram for (0 and 1)", use_container_width=True)
        except Exception as e:
            st.error(f"Error loading CFG image: {str(e)}")

with tab3:
    st.title("PDA Visualization")
    pda_language = st.selectbox(
        "Select PDA Pattern:",
        ["(a and b)", "(0 and 1)"],
        key="pda_language"
    )
    
    if pda_language == "(a and b)":
        st.write("PDA Visualization for (a and b) pattern")
        try:
            pda_image = Image.open("494813958_1219890723098024_7236129594408158240_n.jpg")
            st.image(pda_image, caption="PDA Diagram for (a and b)", use_container_width=True)
        except Exception as e:
            st.error(f"Error loading PDA image: {str(e)}")
    else:
        st.write("PDA Visualization for (0 and 1) pattern")
        try:
            pda_image = Image.open("494691865_919895100199682_529064143852684040_n.jpg")
            st.image(pda_image, caption="PDA Diagram for (0 and 1)", use_container_width=True)
        except Exception as e:
            st.error(f"Error loading PDA image: {str(e)}")

# add helpful information
st.sidebar.title("About")
st.sidebar.info("""
This application visualizes and tests strings against DFA. It would also diplay their respective CFG and PDA diagrams.
- DFA tab: Test strings and see step-by-step simulation
- PDA tab: View the Pushdown Automaton diagram
- CFG tab: View the Context-Free Grammar diagram
""")

