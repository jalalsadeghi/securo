import { useState } from 'react';
import { createAgent } from '../utils/api';

export default function AgentCreateForm() {
  const [userId, setUserId] = useState("");
  const [agentIdentifier, setAgentIdentifier] = useState("");
  const [deviceName, setDeviceName] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const result = await createAgent(parseInt(userId), agentIdentifier, deviceName);
      alert(`Agent created: ${result.agent_identifier}`);
    } catch (error) {
      alert(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="number"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
        placeholder="User ID"
        required
      />
      <input
        type="text"
        value={agentIdentifier}
        onChange={(e) => setAgentIdentifier(e.target.value)}
        placeholder="Agent Identifier"
        required
      />
      <input
        type="text"
        value={deviceName}
        onChange={(e) => setDeviceName(e.target.value)}
        placeholder="Device Name"
        required
      />
      <button type="submit">Create Agent</button>
    </form>
  );
}
