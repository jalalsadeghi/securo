import Link from "next/link";

export default function Home() {
  return (
    <div>
      <h1>Cloud Security Platform</h1>
      <ul>
        <li><Link href="/register">User Registration</Link></li>
        <li><Link href="/agents">Manage Agents</Link></li>
      </ul>
    </div>
  );
}
