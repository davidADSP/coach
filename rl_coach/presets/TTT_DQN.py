from rl_coach.agents.dqn_agent import DQNAgentParameters
from rl_coach.base_parameters import VisualizationParameters, PresetValidationParameters
from rl_coach.environments.environment import SingleLevelSelection
from rl_coach.environments.gym_environment import GymVectorEnvironment, ObservationSpaceType, atari_deterministic_v4, atari_schedule
from rl_coach.graph_managers.basic_rl_graph_manager import BasicRLGraphManager
from rl_coach.filters.filter import NoInputFilter, NoOutputFilter

#########
# Agent #
#########
agent_params = DQNAgentParameters()
# since we are using Adam instead of RMSProp, we adjust the learning rate as well
agent_params.network_wrappers['main'].learning_rate = 0.0001

###############
# Environment #
###############

# env_params = GymVectorEnvironment(level = "rl_coach.environments.ttt:TicTacToeEnv")
env_params = GymVectorEnvironment(level = "rl_coach.environments.ttt:TicTacToeEnv")


# env_params.observation_space_type = ObservationSpaceType.Vector
########
# Test #
########
preset_validation_params = PresetValidationParameters()
preset_validation_params.trace_test_levels = ['breakout', 'pong', 'space_invaders']

graph_manager = BasicRLGraphManager(agent_params=agent_params, env_params=env_params,
                                    schedule_params=atari_schedule, vis_params=VisualizationParameters(),
                                    preset_validation_params=preset_validation_params)
