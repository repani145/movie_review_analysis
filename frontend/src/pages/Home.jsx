import Header from "../components/Header";

import ReviewInput from "../components/ReviewInput";

function Home() {
    return (
        <div className="min-h-screen flex flex-col items-center justify-start">
            <Header />

            <main className="w-full max-w-4xl px-6 mt-8 -translate-y-6">
                <ReviewInput />
            </main>
        </div>
    );
}

export default Home;