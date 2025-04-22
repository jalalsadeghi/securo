export const registerUser = async (email: string, password: string) => {
  const response = await fetch("http://localhost:8000/users/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  if (!response.ok) {
    const errorDetail = await response.text();
    throw new Error(`Registration failed: ${errorDetail}`);
  }
  return response.json();
};

export const createAgent = async (userId: number, agent_identifier: string, device_name: string) => {
  const response = await fetch(`http://localhost:8000/agents/${userId}/create`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ agent_identifier, device_name }),
  });

  if (!response.ok) {
    const errorDetail = await response.text();
    throw new Error(`Agent creation failed: ${errorDetail}`);
  }
  return response.json();
};
