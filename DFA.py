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
    
def draw_dfa(dfa, active_state=None, active_edge=None):
    """Draw the DFA highlighting the active_state and optionally an active_edge (transition)."""
    dot = graphviz.Digraph()  
    dot.attr(rankdir='LR', size="20,8")
   

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
        edge_kwargs = {}
        if active_edge and (from_state, symbol, to_state) == active_edge:
            edge_kwargs = {'color': 'darkgreen', 'penwidth': '3'}
        if from_state == to_state:
            # Self-loop
            dot.edge(from_state, to_state, label=symbol, 
                    constraint='false', **edge_kwargs)
        else:
            dot.edge(from_state, to_state, label=symbol, 
                    constraint='true', **edge_kwargs)

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

states_01 = {'s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16', 's17', 's18', 's19', 's20', 's21', 's22', 's23', 's24', 's25', 's26', 's27', 's28', 's29', 's30', 's31', 's32', 's33', 's34', 's35', 's36', 's37', 's38', 's39', 's40', 's41', 's42', 's43', 's44', 's45', 's46', 's47', 's48', 's49', 's50', 's51', 's52', 's53', 's54', 's55', 's56', 's57', 's58', 's59', 's60', 's61', 's62', 's63', 's64', 's65', 's66', 's67', 's68', 's69', 's70', 's71', 's72', 's73', 's74', 's75', 's76', 's77', 's78', 's79', 's80', 's81', 's82', 's83', 's84', 's85', 's86', 's87', 's88', 's89', 's90', 's91', 's92', 's93', 's94', 's95', 's96', 's97', 's98', 's99', 's100', 's101', 's102', 's103', 's104', 's105', 's106', 's107', 's108', 's109', 's110', 's111', 's112', 's113', 's114', 's115', 's116', 's117', 's118', 's119', 's120', 's121', 's122', 's123', 's124', 's125', 's126', 's127', 's128', 's129', 's130', 's131', 's132', 's133', 's134', 's135', 's136', 's137', 's138', 's139', 's140', 's141', 's142', 's143', 's144', 's145', 's146', 's147', 's148', 's149', 's150', 's151', 's152', 's153', 's154', 's155', 's156', 's157', 's158', 's159', 's160', 's161', 's162', 's163', 's164', 's165', 's166', 's167', 's168', 's169', 's170', 's171', 's172', 's173', 's174', 's175', 's176', 's177', 's178', 's179', 's180', 's181', 's182', 's183', 's184', 's185', 's186', 's187', 's188', 's189', 's190', 's191', 's192', 's193', 's194', 's195', 's196', 's197', 's198', 's199', 's200', 's201', 's202', 's203', 's204', 's205', 's206', 's207', 's208', 's209', 's210', 's211', 's212', 's213', 's214', 's215', 's216', 's217', 's218', 's219', 's220', 's221', 's222', 's223', 's224', 's225', 's226', 's227', 's228', 's229', 's230', 's231', 's232', 's233', 's234', 's235', 's236', 's237', 's238', 's239', 's240', 's241', 's242', 's243', 's244', 's245', 's246', 's247', 's248', 's249', 's250', 's251', 's252', 's253', 's254', 's255', 's256', 's257', 's258', 's259', 's260', 's261', 's262', 's263', 's264', 's265', 's266', 's267', 's268', 's269', 's270', 's271', 's272', 's273', 's274', 's275', 's276', 's277', 's278', 's279', 's280', 's281', 's282', 's283', 's284', 's285', 's286', 's287', 's288', 's289', 's290', 's291', 's292', 's293', 's294', 's295', 's296', 's297', 's298', 's299', 's300', 's301', 's302', 's303', 's304', 's305', 's306', 's307', 's308', 's309', 's310', 's311', 's312', 's313', 's314', 's315', 's316', 's317', 's318', 's319', 's320', 's321', 's322', 's323', 's324', 's325', 's326', 's327', 's328', 's329', 's330', 's331', 's332', 's333', 's334', 's335', 's336', 's337', 's338', 's339', 's340', 's341', 's342', 's343', 's344', 's345', 's346', 's347', 's348', 's349', 's350', 's351', 's352', 's353', 's354', 's355', 's356', 's357', 's358', 's359', 's360', 's361', 's362', 's363', 's364', 's365', 's366', 's367', 's368', 's369', 's370', 's371', 's372', 's373', 's374', 's375', 's376', 's377', 's378', 's379', 's380', 's381', 's382', 's383', 's384', 's385', 's386', 's387', 's388', 's389', 's390', 's391', 's392', 's393', 's394', 's395', 's396', 's397', 's398', 's399', 's400', 's401', 's402', 's403', 's404', 's405', 's406', 's407', 's408', 's409', 's410', 's411', 's412', 's413', 's414', 's415', 's416', 's417', 's418', 's419', 's420', 's421', 's422', 's423', 's424', 's425', 's426', 's427', 's428', 's429', 's430', 's431', 's432', 's433', 's434', 's435', 's436', 's437', 's438', 's439', 's440', 's441', 's442', 's443', 's444', 's445', 's446', 's447', 's448', 's449', 's450', 's451', 's452', 's453', 's454', 's455', 's456', 's457', 's458', 's459', 's460', 's461', 's462', 's463', 's464', 's465', 's466', 's467', 's468', 's469', 's470', 's471', 's472', 's473', 's474', 's475', 's476', 's477', 's478', 's479', 's480', 's481', 's482', 's483', 's484', 's485', 's486', 's487', 's488', 's489', 's490', 's491', 's492', 's493', 's494', 's495', 's496', 's497', 's498', 's499', 's500', 's501', 's502', 's503', 's504', 's505', 's506', 's507', 's508', 's509', 's510', 's511', 's512', 's513', 's514', 's515', 's516', 's517', 's518', 's519', 's520', 's521', 's522', 's523', 's524', 's525', 's526', 's527', 's528', 's529', 's530', 's531', 's532', 's533', 's534', 's535', 's536', 's537', 's538', 's539', 's540', 's541', 's542', 's543', 's544', 's545', 's546', 's547', 's548', 's549', 's550', 's551', 's552', 's553', 's554', 's555', 's556', 's557', 's558', 's559', 's560', 's561', 's562', 's563', 's564', 's565', 's566', 's567', 's568', 's569', 's570', 's571', 's572', 's573', 's574', 's575', 's576', 's577', 's578', 's579', 's580', 's581', 's582', 's583', 's584', 's585', 's586', 's587', 's588', 's589', 's590', 's591', 's592', 's593', 's594', 's595', 's596', 's597', 's598', 's599', 's600', 's601', 's602', 's603', 's604', 's605', 's606', 's607', 's608', 's609', 's610', 's611', 's612', 's613', 's614', 's615', 's616', 's617', 's618', 's619', 's620', 's621', 's622', 's623', 's624', 's625', 's626', 's627', 's628', 's629', 's630', 's631', 's632', 's633', 's634', 's635', 's636', 's637', 's638', 's639', 's640', 's641', 's642', 's643', 's644', 's645', 's646', 's647', 's648', 's649', 's650', 's651', 's652', 's653', 's654', 's655', 's656', 's657', 's658', 's659', 's660', 's661', 's662', 's663', 's664', 's665', 's666', 's667', 's668', 's669', 's670', 's671', 's672', 's673', 's674', 's675', 's676', 's677', 's678', 's679', 's680', 's681', 's682', 's683', 's684', 's685', 's686', 's687', 's688', 's689', 's690', 's691', 's692', 's693', 's694', 's695', 's696', 's697', 's698', 's699', 's700', 's701', 's702', 's703', 's704', 's705', 's706', 's707', 's708', 's709', 's710', 's711', 's712', 's713', 's714', 's715', 's716', 's717', 's718', 's719', 's720', 's721', 's722', 's723', 's724', 's725', 's726', 's727', 's728', 's729', 's730', 's731', 's732', 's733', 's734', 's735', 's736', 's737', 's738', 's739', 's740', 's741', 's742', 's743', 's744', 's745', 's746', 's747', 's748', 's749', 's750', 's751', 's752', 's753', 's754', 's755', 's756', 's757', 's758', 's759', 's760', 's761', 's762', 's763', 's764', 's765', 's766', 's767', 's768', 's769', 's770', 's771', 's772', 's773', 's774', 's775', 's776', 's777', 's778', 's779', 's780', 's781', 's782', 's783', 's784', 's785', 's786', 's787', 's788', 's789', 's790', 's791', 's792', 's793', 's794', 's795', 's796', 's797', 's798', 's799', 's800', 's801', 's802', 's803', 's804', 's805', 's806', 's807', 's808', 's809', 's810', 's811', 's812', 's813', 's814', 's815', 's816', 's817', 's818', 's819', 's820', 's821', 's822', 's823', 's824', 's825', 's826', 's827', 's828', 's829', 's830', 's831', 's832', 's833', 's834', 's835', 's836', 's837', 's838', 's839', 's840', 's841', 's842', 's843', 's844', 's845', 's846', 's847', 's848', 's849', 's850', 's851', 's852', 's853', 's854', 's855', 's856', 's857', 's858', 's859', 's860', 's861', 's862', 's863', 's864', 's865', 's866', 's867', 's868', 's869', 's870', 's871', 's872', 's873', 's874', 's875', 's876', 's877', 's878', 's879', 's880', 's881', 's882', 's883', 's884', 's885', 's886', 's887', 's888', 's889', 's890', 's891', 's892', 's893', 's894', 's895', 's896', 's897', 's898', 's899', 's900', 's901', 's902', 's903', 's904', 's905', 's906', 's907', 's908', 's909', 's910', 's911', 's912', 's913', 's914', 's915', 's916', 's917', 's918', 's919', 's920', 's921', 's922', 's923', 's924', 's925', 's926', 's927', 's928', 's929', 's930', 's931', 's932', 's933', 's934', 's935', 's936', 's937', 's938', 's939', 's940', 's941', 's942', 's943', 's944', 's945', 's946', 's947', 's948', 's949', 's950', 's951', 's952', 's953', 's954', 's955', 's956', 's957', 's958', 's959', 's960', 's961', 's962', 's963', 's964', 's965', 's966', 's967', 's968', 's969', 's970', 's971', 's972', 's973', 's974', 's975', 's976', 's977', 's978', 's979', 's980', 's981', 's982', 's983', 's984', 's985', 's986', 's987', 's988', 's989', 's990', 's991', 's992', 's993', 's994', 's995', 's996', 's997', 's998', 's999', 's1000', 'sF'}
alphabet_01 = {'0', '1'}
transition_function_01 = {
    # Initial states for (1*01*01*)
    ('s0', '1'): 's0',
    ('s0', '0'): 's1',
    ('s1', '1'): 's1',
    ('s1', '0'): 's2',
    ('s2', '1'): 's2',
    
    # (11+00)
    ('s2', '1'): 's3',
    ('s2', '0'): 's4',
    ('s3', '1'): 's5',
    ('s4', '0'): 's5',
    
    # (10+01)*
    ('s5', '1'): 's6',
    ('s5', '0'): 's7',
    ('s6', '0'): 's5',
    ('s7', '1'): 's5',
    
    # (1+0)
    ('s5', '1'): 's8',
    ('s5', '0'): 's8',
    
    # (11+00)
    ('s8', '1'): 's9',
    ('s8', '0'): 's10',
    ('s9', '1'): 's11',
    ('s10', '0'): 's11',
    
    # (1+0+11+00+101+111+000)
    ('s11', '1'): 's12',
    ('s11', '0'): 's12',
    ('s12', '1'): 's13',
    ('s12', '0'): 's13',
    ('s13', '1'): 's14',
    ('s13', '0'): 's14',
    
    # (11+00)*
    ('s14', '1'): 's15',
    ('s14', '0'): 's16',
    ('s15', '1'): 's14',
    ('s16', '0'): 's14',
    
    # (10*10*1)
    ('s14', '1'): 's17',
    ('s17', '0'): 's17',
    ('s17', '1'): 's18',
    ('s18', '0'): 's18',
    ('s18', '1'): 's19',
    
    # (11+00)
    ('s19', '1'): 's20',
    ('s19', '0'): 's21',
    ('s20', '1'): 'sF',
    ('s21', '0'): 'sF',
    
    # Final state transitions
    ('sF', '0'): 'sF',
    ('sF', '1'): 'sF'
}

start_state_01 = 's0'
accept_states_01 = {'sF'}
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
        dfa_pattern = "This DFA matches the pattern: (a+b)\* (aa+bb) (aa+bb)\* (ab+ba+aba) (bab+aba+bbb) (a+b+aa+bb)\* (bb+aa+aba) (aaa+bba+bab) (aaa+bba+bab)\*"
        st.sidebar.title("Valid String Examples")
        st.sidebar.code("""
        baabbabaabaababba
        bbabababbbbab
        bbbabbbbbbab
        aaababbbbbaaa
        aabababbbbba
        """)
    else:
        dfa = dfa_01
        alphabet = alphabet_01
        dfa_title = "🌟 DFA Compiler & Visualizer (0 and 1)"
        dfa_pattern = "This DFA matches 
        st.sidebar.code("""
        101011101101
        010110101000
        0011000111
        010110101001
        11111111111
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
                                    if step_idx > 0:
                                        prev_state, _ = path[step_idx - 1]
                                        active_edge = (prev_state, symbol, state)
                                    else:
                                        active_edge = None
                                    dfa_placeholder.graphviz_chart(draw_dfa(dfa, active_state=state, active_edge=active_edge))
                                    
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
            pda_image = Image.open("494359347_2295752140838959_2054055215976526836_n.jpg")
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

