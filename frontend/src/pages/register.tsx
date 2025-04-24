import UserRegisterForm from "@/components/UserRegisterForm";

export default function Register() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="w-full max-w-md p-8 space-y-6 bg-white shadow-md rounded-2xl">
        <h2 className="text-2xl font-bold text-center text-primary">User Registration</h2>
        <UserRegisterForm />
      </div>
    </div>
  );
}
