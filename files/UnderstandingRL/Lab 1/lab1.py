import gymnasium as gym

# Create the environment
env = gym.make("CartPole-v1")

# Reset the environment
observation, info = env.reset()

for _ in range(1000):
    env.render()

    # Random action in the action space
    action = env.action_space.sample()

    # Apply the action to the environment
    observation, reward, done, truncated, info = env.step(action)

    # Check if the episode is over
    if done or truncated:
        observation, info = env.reset()

# Close the environment
env.close()
