import React from "react";

function Navbar() {
  return (
      <div>
        <nav className="navbar navbar-expand-lg border-bottom py-3 bg-light sticky-top" style={{backgroundColor: (0,0,0, 0.25)}}>
          <div className="container">
            <a className="navbar-brand" href="/">
              Scoop
            </a>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarSupportedContent">
              <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
                <li className="nav-item">
                  <a className="btn btn-light nav-link" aria-current="page" href="/">
                    Home
                  </a>
                </li>
                <li className="nav-item">
                  <a className="btn btn-light nav-link" aria-current="page" href="/login/">
                    Login
                  </a>
                </li>
                <li className="nav-item">
                  <a className="btn btn-light nav-link" aria-current="page" href="/register/">
                    Register
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
  );
}

export default Navbar;
