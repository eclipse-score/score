/* *******************************************************************************
 * Copyright (c) 2024 Contributors to the Eclipse Foundation
 *
 * SPDX-License-Identifier: Apache-2.0
 * *******************************************************************************
 *
 * Adds collapse/expand toggle arrows to the left-sidebar navigation tree.
 * Top-level entries (toctree-l1) that have nested children get a clickable ▸/▾ arrow.
 */

(function () {
    function initTocCollapse() {
        const tocNav = document.querySelector(".bd-sidebar-primary .bd-links, .bd-sidebar-primary nav");
        if (!tocNav) return;

        // Find all toctree entries that have a nested <ul>
        const h2Items = tocNav.querySelectorAll("li.toctree-l1");

        h2Items.forEach(function (li) {
            const childUl = li.querySelector(":scope > ul");
            if (!childUl) return;

            // Create toggle button
            const toggle = document.createElement("span");
            toggle.className = "toc-toggle";
            toggle.setAttribute("aria-label", "Toggle section");
            toggle.innerHTML = "▸";
            toggle.style.cssText = [
                "cursor: pointer",
                "display: inline-block",
                "margin-right: 0.3em",
                "font-size: 0.75em",
                "transition: transform 0.15s ease",
                "color: var(--pst-color-secondary)",
                "vertical-align: middle",
                "user-select: none",
            ].join(";");

            // Start collapsed
            childUl.style.cssText = "overflow: hidden; height: 0; display: block; transition: height 0.2s ease;";

            // Prepend toggle to the <a> link (left nav uses plain <a>, not a.nav-link)
            const link = li.querySelector(":scope > a");
            if (link) link.prepend(toggle);

            toggle.addEventListener("click", function (e) {
                e.preventDefault();
                e.stopPropagation();
                const isOpen = childUl.dataset.open === "1";
                if (isOpen) {
                    childUl.style.height = childUl.scrollHeight + "px";
                    requestAnimationFrame(function () {
                        childUl.style.height = "0";
                    });
                    childUl.dataset.open = "0";
                    toggle.style.transform = "rotate(0deg)";
                } else {
                    childUl.style.height = childUl.scrollHeight + "px";
                    childUl.dataset.open = "1";
                    toggle.style.transform = "rotate(90deg)";
                    // After transition, remove fixed height so it can reflow
                    childUl.addEventListener("transitionend", function onEnd() {
                        if (childUl.dataset.open === "1") childUl.style.height = "auto";
                        childUl.removeEventListener("transitionend", onEnd);
                    });
                }
            });

            // Auto-expand the section that contains the active link (left nav uses class 'current')
            if (li.classList.contains("current") || li.querySelector("a.current, a.active")) {
                childUl.style.height = "auto";
                childUl.dataset.open = "1";
                toggle.style.transform = "rotate(90deg)";
            }
        });
    }

    // Run after DOM is ready
    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initTocCollapse);
    } else {
        initTocCollapse();
    }
})();
