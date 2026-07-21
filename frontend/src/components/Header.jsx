import robot from "../assets/robot.svg";

function Header() {
    return (
        <header className="hero min-h-[60vh] flex items-center justify-center text-center px-6">
            <div>
                <h1 className="hero-title text-[3.2rem] md:text-[4rem] leading-tight font-extrabold">
                    <span className="mona">MOVIE</span>
                    <span className="ampersand"> REVIEW </span>
                    <span className="hubot">ANALYZER</span>
                </h1>

                <p className="subtitle mt-4 text-sm md:text-base text-slate-300/80">
                    AI-powered sentiment insights
                </p>

                <div className="robot-wrap mx-auto mt-8 w-44 md:w-56">
                    <img src={robot} alt="robot mascot" className="robot w-full h-auto" />
                </div>
            </div>
        </header>
    );
}

export default Header;