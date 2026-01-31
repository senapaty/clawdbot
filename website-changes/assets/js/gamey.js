// Gamey Design Elements - Subtle Easter Eggs

(function() {
    'use strict';
    
    // HP Bar (Reading Progress)
    function createHPBar() {
        const container = document.createElement('div');
        container.className = 'hp-bar-container';
        container.innerHTML = '<div class="hp-bar" id="hpBar"></div>';
        document.body.prepend(container);
        
        // XP bar (secondary)
        const xpContainer = document.createElement('div');
        xpContainer.className = 'xp-bar';
        xpContainer.innerHTML = '<div class="xp-fill" id="xpFill"></div>';
        document.body.prepend(xpContainer);
        
        window.addEventListener('scroll', updateHPBar);
        updateHPBar();
    }
    
    function updateHPBar() {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollPercent = (scrollTop / docHeight) * 100;
        
        const hpBar = document.getElementById('hpBar');
        const xpFill = document.getElementById('xpFill');
        
        if (hpBar) hpBar.style.width = scrollPercent + '%';
        if (xpFill) xpFill.style.width = scrollPercent + '%';
        
        // Check achievements based on scroll
        checkScrollAchievements(scrollPercent);
    }
    
    // Achievement System
    const achievements = {
        firstScroll: { unlocked: false, title: "First Steps", text: "Started your journey", icon: "👣" },
        halfway: { unlocked: false, title: "Halfway There", text: "50% complete - Keep going!", icon: "🎯" },
        completionist: { unlocked: false, title: "Completionist", text: "100% - You read everything!", icon: "🏆" },
        speedReader: { unlocked: false, title: "Speed Reader", text: "Scrolled through quickly", icon: "⚡" },
        deepDiver: { unlocked: false, title: "Deep Diver", text: "Explored all sections", icon: "🔍" }
    };
    
    let scrollStartTime = Date.now();
    
    function checkScrollAchievements(percent) {
        if (percent > 5 && !achievements.firstScroll.unlocked) {
            unlockAchievement('firstScroll');
        }
        if (percent >= 50 && !achievements.halfway.unlocked) {
            unlockAchievement('halfway');
        }
        if (percent >= 100 && !achievements.completionist.unlocked) {
            unlockAchievement('completionist');
        }
        
        // Speed reader check
        const timeSpent = (Date.now() - scrollStartTime) / 1000;
        if (percent >= 90 && timeSpent < 30 && !achievements.speedReader.unlocked) {
            unlockAchievement('speedReader');
        }
    }
    
    function unlockAchievement(key) {
        achievements[key].unlocked = true;
        showAchievement(achievements[key]);
    }
    
    function showAchievement(achievement) {
        const div = document.createElement('div');
        div.className = 'achievement';
        div.innerHTML = `
            <span class="achievement-icon">${achievement.icon}</span>
            <div style="display: inline-block; vertical-align: middle;">
                <div class="achievement-title">Achievement Unlocked</div>
                <div class="achievement-text"><strong>${achievement.title}</strong> - ${achievement.text}</div>
            </div>
        `;
        document.body.appendChild(div);
        
        // Trigger animation
        setTimeout(() => div.classList.add('show'), 100);
        
        // Remove after 4 seconds
        setTimeout(() => {
            div.classList.remove('show');
            setTimeout(() => div.remove(), 500);
        }, 4000);
    }
    
    // Konami Code Easter Egg
    const konamiCode = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
    let konamiIndex = 0;
    
    document.addEventListener('keydown', (e) => {
        if (e.key === konamiCode[konamiIndex]) {
            konamiIndex++;
            if (konamiIndex === konamiCode.length) {
                activateKonami();
                konamiIndex = 0;
            }
        } else {
            konamiIndex = 0;
        }
    });
    
    function activateKonami() {
        document.body.classList.add('konami-active');
        showAchievement({
            icon: "🎮",
            title: "Konami Code",
            text: "Cheat activated! Try the terminal mode button"
        });
        
        // Show terminal button if hidden
        const btn = document.getElementById('terminalBtn');
        if (btn) btn.style.display = 'flex';
        
        setTimeout(() => {
            document.body.classList.remove('konami-active');
        }, 1000);
    }
    
    // Terminal Mode Toggle
    function createTerminalButton() {
        const btn = document.createElement('button');
        btn.id = 'terminalBtn';
        btn.className = 'terminal-mode-btn';
        btn.innerHTML = '⌨️';
        btn.title = 'Toggle Terminal Mode';
        btn.style.display = 'none'; // Hidden until Konami code
        btn.onclick = toggleTerminalMode;
        document.body.appendChild(btn);
    }
    
    function toggleTerminalMode() {
        document.body.classList.toggle('terminal-mode');
        const isTerminal = document.body.classList.contains('terminal-mode');
        
        if (isTerminal) {
            showAchievement({
                icon: "💻",
                title: "Terminal Mode",
                text: "Welcome to the matrix, Neo"
            });
        }
        
        // Save preference
        localStorage.setItem('terminalMode', isTerminal);
    }
    
    // Cheat hint
    function createCheatHint() {
        const hint = document.createElement('div');
        hint.className = 'cheat-hint';
        hint.textContent = '↑↑↓↓←→←→BA';
        document.body.appendChild(hint);
    }
    
    // Initialize
    document.addEventListener('DOMContentLoaded', () => {
        createHPBar();
        createTerminalButton();
        createCheatHint();
        
        // Restore terminal mode if previously set
        if (localStorage.getItem('terminalMode') === 'true') {
            document.body.classList.add('terminal-mode');
            const btn = document.getElementById('terminalBtn');
            if (btn) btn.style.display = 'flex';
        }
        
        // After 10 seconds, show terminal button hint
        setTimeout(() => {
            const btn = document.getElementById('terminalBtn');
            if (btn && btn.style.display === 'none') {
                btn.style.opacity = '0.3';
                btn.style.display = 'flex';
            }
        }, 10000);
    });
    
    // Click counter easter egg
    let clickCount = 0;
    document.addEventListener('click', () => {
        clickCount++;
        if (clickCount === 50) {
            unlockAchievement({
                icon: "🖱️",
                title: "Click Master",
                text: "50 clicks! You're engaged!"
            });
        }
    });
    
})();
