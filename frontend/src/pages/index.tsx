import { Button } from "@/components/ui/button";
import Link from "next/link";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen space-y-6">
      <h1 className="text-4xl font-bold text-primary">Cloud Security Platform</h1>
      <div className="flex gap-4">
        <Button asChild>
          <Link href="/register">User Registration</Link>
        </Button>
        <br></br>
        <Button asChild>
          <Link href="/agents">Manage Agents</Link>
        </Button>
      </div>
    </div>
  );
}
