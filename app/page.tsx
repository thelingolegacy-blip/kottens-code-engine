import "./globals.css";

const lanes = [
  ["WATCH", "Stories and adventures", "Start an episode"],
  ["PLAY", "Games and discoveries", "Play now"],
  ["READ", "Books and storytime", "Open library"],
  ["COLLECT", "Books and keepsakes", "Explore books"],
];

function SoundHalo() {
  return <div className="sound-halo" aria-hidden="true"><i/><i/><i/><span>♪</span></div>;
}

export default function Home() {
  return (
    <main className="world">
      <div className="sky-noise" aria-hidden="true" />
      <div className="cloud cloud-a" aria-hidden="true" />
      <div className="cloud cloud-b" aria-hidden="true" />
      <header className="nav">
        <strong>KottonsCode</strong>
        <nav aria-label="Primary"><a href="#watch">Watch</a><a href="#play">Play</a><a href="#read">Read</a><a href="#parents">Parents</a></nav>
      </header>
      <section className="hero" aria-labelledby="title">
        <div className="kotton-orb" role="img" aria-label="Kotton floating in Kotton&apos;s cloud world">🐾</div>
        <SoundHalo />
        <p className="eyebrow">KOTTONSCODE STUDIO</p>
        <h1 id="title">Welcome to Kotton&apos;s World</h1>
        <p className="lead">Stories, games, books, and adventures floating in the sky.</p>
        <a className="primary" href="#studio">Enter Kotton&apos;s World <span aria-hidden="true">→</span></a>
      </section>
      <section id="studio" className="studio" aria-labelledby="studio-title">
        <div><p className="eyebrow">THE WORLD HUB</p><h2 id="studio-title">Pick your adventure</h2></div>
        <div className="lanes">
          {lanes.map(([title, description, action], index) => <article className={`lane lane-${index + 1}`} id={title.toLowerCase()} key={title}>
            <SoundHalo /><span className="lane-number">0{index + 1}</span><h3>{title}</h3><p>{description}</p><button type="button">{action} <span aria-hidden="true">↗</span></button>
          </article>)}
        </div>
      </section>
      <section id="parents" className="parents"><p className="eyebrow">FOR GROWN-UPS</p><h2>A playful world with a parent-safe doorway.</h2><p>Safety, learning information, privacy, and account controls live behind the Parent Zone.</p></section>
      <footer>© KottonsCode Studio · Safe, playful, imaginative.</footer>
    </main>
  );
}
