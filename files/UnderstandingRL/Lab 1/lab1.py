import gymnasium as gym

# Create the environment with render_mode
env = gym.make("CartPole-v1", render_mode="human")

# Reset the environment
observation, info = env.reset()

for _ in range(1000):
    # Render the environment
    env.render()

    # Take a random action
    action = env.action_space.sample()

    # Apply the action to the environment
    observation, reward, done, truncated, info = env.step(action)

    if done or truncated:
        observation, info = env.reset()

# Close the environment
env.close()
