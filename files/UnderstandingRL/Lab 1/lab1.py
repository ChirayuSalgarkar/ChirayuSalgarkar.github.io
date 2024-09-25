
import numpy as np
import gymnasium as gym
import matplotlib.pyplot as plt

# Set up the CartPole-v0 environment
env = gym.make('CartPole-v1')

# Define the number of bins for each state variable
bins = [
    np.linspace(-2.4, 2.4, 10),  # Cart Position
    np.linspace(-3.0, 3.0, 10),  # Cart Velocity
    np.linspace(-0.21, 0.21, 10),  # Pole Angle
    np.linspace(-2.0, 2.0, 10)  # Pole Velocity at Tip
]

# Function to discretize the continuous state into a discrete state
def discretize_state(state):
    discrete_state = []
    for i, bin_edges in enumerate(bins):
        discrete_state.append(np.digitize(state[i], bin_edges) - 1)
    return tuple(discrete_state)

# Policy Iteration Algorithm
def policy_iteration(env, policy, gamma=0.99, theta=1e-4):
    V = np.zeros(env.observation_space.n)
    while True:
        # Policy Evaluation
        delta = 0
        for s in range(env.observation_space.n):
            v = V[s]
            V[s] = sum([p * (r + gamma * V[s_])
                        for p, s_, r, _ in env.P[s][policy[s]]])
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break

    # Policy Improvement
    policy_stable = True
    for s in range(env.observation_space.n):
        old_action = policy[s]
        policy[s] = np.argmax([sum([p * (r + gamma * V[s_])
                                    for p, s_, r, _ in env.P[s][a]])
                               for a in range(env.action_space.n)])
        if old_action != policy[s]:
            policy_stable = False
    return policy, V

# SARSA Algorithm
def sarsa(env, episodes=10000, alpha=0.1, gamma=0.99, epsilon=0.1):
    Q = np.zeros((env.observation_space.n, env.action_space.n))
    for episode in range(episodes):
        state, _ = env.reset()
        state = discretize_state(state)
        action = np.random.choice(env.action_space.n) if np.random.rand() < epsilon else np.argmax(Q[state])
        done = False
        while not done:
            next_state, reward, done, _, _ = env.step(action)
            next_state = discretize_state(next_state)
            next_action = np.random.choice(env.action_space.n) if np.random.rand() < epsilon else np.argmax(Q[next_state])
            Q[state][action] += alpha * (reward + gamma * Q[next_state][next_action] - Q[state][action])
            state, action = next_state, next_action
    return Q

# Q-Learning Algorithm
def q_learning(env, episodes=10000, alpha=0.1, gamma=0.99, epsilon=0.1):
    Q = np.zeros((env.observation_space.n, env.action_space.n))
    for episode in range(episodes):
        state, _ = env.reset()
        state = discretize_state(state)
        done = False
        while not done:
            action = np.random.choice(env.action_space.n) if np.random.rand() < epsilon else np.argmax(Q[state])
            next_state, reward, done, _, _ = env.step(action)
            next_state = discretize_state(next_state)
            Q[state][action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state][action])
            state = next_state
    return Q

# Monte Carlo Prediction Algorithm
def monte_carlo(env, episodes=10000, gamma=0.99):
    V = np.zeros(env.observation_space.n)
    returns = {state: [] for state in range(env.observation_space.n)}
    
    for episode in range(episodes):
        episode_data = []
        state, _ = env.reset()
        state = discretize_state(state)
        done = False
        while not done:
            action = np.random.choice(env.action_space.n)
            next_state, reward, done, _, _ = env.step(action)
            episode_data.append((state, reward))
            state = discretize_state(next_state)
        
        G = 0
        for t in reversed(range(len(episode_data))):
            state, reward = episode_data[t]
            G = gamma * G + reward
            if state not in [x[0] for x in episode_data[:t]]:
                returns[state].append(G)
                V[state] = np.mean(returns[state])
    return V

# Plot learning curves
def plot_learning_curve(data, label):
    plt.plot(data, label=label)
    plt.xlabel('Episodes')
    plt.ylabel('Average Reward')
    plt.legend()
    plt.show()
